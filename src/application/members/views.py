"""This module contains the views for the members package.

.. module:: application.members.views

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

from flaskext.flask_login import current_user, login_required

from application import app

from application.accounts.accounts import require_roles, find_users
from application.accounts import accounts

from application.accounts.models import RoleModel, UserRoleModel

import forms
import models
from members import get_family_choices, get_role_choices
from members import send_new_user_mail
from members import get_avatar_url
from members import check_permissions
from members import permission_denied

from flask import render_template, flash, url_for, redirect, request, jsonify

from google.appengine.api import mail


@app.route('/members/create', methods=['GET', 'POST'])
@require_roles(names=['webmaster', 'membership'])
def create_user():
    """
    View for creating a user
    """

    from application.generate_keys import generate_randomkey
    
    form = forms.CreateUserForm(request.form)

    form.family.choices = get_family_choices()
    
    form.roles.choices = get_role_choices()

    if request.method == 'POST':
        if form.validate():
            # create the user with information specified in form
            fname = form.fname.data
            lname = form.lname.data
            cwruid = form.cwruid.data

            # generate a new temporary password
            password = generate_randomkey(16)

            # get optional attributes
            optional_attr = {}
            if form.mname.data != '':
                optional_attr['mname'] = form.mname.data
                
            if form.family.data != 'none':
                # look up family instance
                query = models.FamilyModel.all()
                query.filter('name =', form.family.data)
                families = query.fetch(1)
                if len(families) != 1:
                    form.family.errors.append(u'Family %s does not exist' % form.family.data)
                    return render_template('members/create.html',
                                           create_user_form=form)
                optional_attr['family'] = families[0].key()
                
            if form.big.data != '':
                # look up big instance
                users = find_users(cwruid=('=', form.big.data))
                if len(users) != 1:
                    form.big.errors.append(u'User %s does not exist' % form.big.data)
                    return render_template('members/create.html',
                                           create_user_form=form)
                optional_attr['big'] = users[0].key()
                
            if form.avatar.data != '':
                optional_attr['avatar'] = form.avatar.data
            
            try:
                new_user = accounts.create_user(fname, lname, cwruid, password, **optional_attr)
                if new_user is None:
                    raise AttributeError('Something went wrong with user creation')

                # add the case email address to the user
                email = models.EmailModel(user=new_user.key(),
                                          email='%s@case.edu' % new_user.cwruid,
                                          name='Case Email')
                email.put()

                # add the roles to the user
                for role in form.roles.data:
                    query = RoleModel.all()
                    query.filter('name =', role)

                    if query.count() != 1:
                        flash('Role %s does not exist' % role, 'error')
                        continue

                    desired_role = query.fetch(1)[0]

                    new_urole = UserRoleModel(user=new_user.key(), role=desired_role.key())
                    new_urole.put()
                    
                flash('User created successfully', 'success')

                form = None
                form = forms.CreateUserForm()
                form.family.choices = get_family_choices()
                form.roles.choices = get_role_choices()

                send_new_user_mail(fname, lname, cwruid, password)
            except AttributeError, e:
                flash(str(e), 'error')
    
    # render the template
    
    return render_template('members/create.html',
                           create_user_form=form)


@app.route('/members/list/', methods=['GET', 'POST'])
@login_required
def list_users():
    """
    View for listing all users
    and listing users based on a
    search.

    If membership role or webmaster role is present
    then the user will also see edit links for the user
    """

    can_edit = None

    query = UserRoleModel.all()
    query.filter('user =', current_user.key())

    uroles = query.fetch(query.count())
    for urole in uroles:
        if urole.role.name == 'webmaster':
            can_edit = True
            break
    
    users = find_users()
    return render_template('members/list.html',
                           can_edit=can_edit,
                           users=users)

@app.route('/members/delete/<cwruid>', methods=['GET'])
@login_required
@require_roles(names=['webmaster', 'membership'])
def delete_user(cwruid):
    """
    When this view receives a GET request, if the
    user has the correct role then the user will
    be deleted
    """

    next_page = 'list_users'
    
    if current_user.cwruid == cwruid:
        flash('Cannot delete account that is currently logged in', 'error')
        return redirect(url_for(next_page))

    try:
        accounts.delete_user(cwruid)
        flash("Successfully deleted account '%s'" % cwruid, 'success')
    except Exception, e:
        flash('Error: %s' % str(e), 'error')

    return redirect(url_for('list_users'))


@app.route('/members/view/<cwruid>', methods=['GET'])
@login_required
def view_user(cwruid):
    """
    This view displays the profile information
    for the request cwruid
    """
    try:
        user = find_users(limit=1, cwruid=('=',cwruid))[0]
    except IndexError:
        return render_template('404.html'), 404

    show_edit_link = False
    permissions = check_permissions(cwruid)
    if permissions[0] or permissions[1]:
        show_edit_link = True

    minitial = ''
    if user.mname is not None and user.mname != '':
        minitial = user.mname[0].capitalize() + '.'

    avatar_address = ''
    if user.avatar is not None:
        avatar_address = user.avatar
        
    avatar = get_avatar_url(avatar_address, request.host_url, size=200)

        
    # get the email addresses associated with this user
    query = models.AddressModel.all()
    query.filter('user =', user.key())
    addresses = query.fetch(query.count())

    query = models.EmailModel.all()
    query.filter('user =', user.key())
    emails = query.fetch(query.count())

    query = models.PhoneModel.all()
    query.filter('user =', user.key())
    numbers = query.fetch(query.count())
    

    family  = None
    if user.family is not None:
        family = user.family.name.title()
    
    return render_template('members/view.html',
                           show_edit_link=show_edit_link,
                           user=user,
                           minitial=minitial,
                           avatar=avatar,
                           family=family,
                           big=user.big,
                           emails=emails,
                           numbers=numbers,
                           addresses=addresses)

@app.route('/members/edit/<cwruid>/account', methods=['GET', 'POST'])
@app.route('/members/edit/<cwruid>', methods=['GET', 'POST'])
@login_required
def display_edit_user_account(cwruid):
    """
    This view allows the user and administrators
    to edit the account information of that user
    """
    import urllib, urlparse

    permissions = check_permissions(cwruid)
    if not permissions[0] and not permissions[1]:
        return permission_denied(cwruid)

    # get the user object for this page
    try:
        user = find_users(1,cwruid=('=', cwruid))[0]
    except IndexError:
        return render_template('404.html'), 404

    main_form = forms.MainUpdateUserForm(None)

    # initialize admin form if this user has
    # admin privileges
    admin_form = None
    if permissions[1]:
        admin_form = forms.AdminUpdateUserForm(None)

        # set the choices
        admin_form.family.choices = get_family_choices()
        admin_form.roles.choices = get_role_choices()

    # populate the main form
    main_form.fname.data = user.fname
    main_form.mname.data = user.mname
    main_form.lname.data = user.lname
    main_form.avatar.data = user.avatar

    # initialize the admin_form if needed
    if admin_form is not None:
        if user.family is not None:
            admin_form.family.data = user.family.name
        if user.big is not None:
            admin_form.big.data = user.big.cwruid

        query = UserRoleModel.all()
        query.filter('user =', user.key())
        uroles = query.fetch(query.count())

        roles = []
        for urole in uroles:
            roles.append(urole.role.name)

        admin_form.roles.data = roles

    return render_template('members/edit_account.html',
                           user=user,
                           permissions=permissions,
                           main_form=main_form,
                           admin_form=admin_form)

@app.route('/members/edit/<cwruid>/account/mainform/json', methods=['POST'])
@login_required
def handle_edit_account_main_json(cwruid):
    """
    This view allows the user and administrators
    to submit an ajax update request
    """

    permissions = check_permissions(cwruid)
    if not permissions[0] and not permissions[1]:
        return jsonify({'result':'failure', 'msg':'Permission denied'})

    main_form = forms.MainUpdateUserForm()

    if main_form.validate():
        try:
            user = find_users(1, cwruid=('=', cwruid))[0]
        except IndexError:
            return jsonify({'result':'failure', 'name':'main', 'errors': {}})

        user.fname = main_form.fname.data
        user.mname = main_form.mname.data
        user.lname = main_form.lname.data
        user.avatar = main_form.avatar.data
        user.save()
        return jsonify({'result':'success'})
    else:
        return jsonify({'result':'failure', 'name':'main', 'errors': main_form.errors})

@app.route('/members/edit/<cwruid>/account/adminform/json', methods=['POST'])
def handle_edit_account_admin_json(cwruid):
    """
    This view handles the AJAX request
    for the AdminUpdateUserForm submission
    from the display_edit_account(cwruid) view
    """
    
    permissions = check_permissions(cwruid)
    if not permissions[0] and not permissions[1]:
        return jsonify({'result':'failure', 'msg':'Permission denied'})

    admin_form = forms.AdminUpdateUserForm()

    # set the choices
    admin_form.family.choices = get_family_choices()
    admin_form.roles.choices = get_role_choices()

    if admin_form.validate():
        try:
            user = find_users(1, cwruid=('=', cwruid))[0]
        except IndexError:
            return jsonify({'result':'failure', 'name':'main', 'errors': {}})

        try:
            big = find_users(1, cwruid=('=', cwruid))[0]
        except IndexError:
            return jsonify({'result':'failure', 'name':'main', 'errors': {}})
        user.big = big.key()

        query = models.FamilyModel.all()
        query.filter('name =', admin_form.family.data)
        try:
            family = query.fetch(query.count())[0]
        except IndexError:
            return jsonify({'result':'failure', 'name':'main', 'errors': {}})
        user.family = family.key()

        query = UserRoleModel.all()
        query.filter('user =', user.key())
        uroles = query.fetch(query.count())
        for role in admin_form.roles.data:

            index = None
            for i, urole in enumerate(uroles):
                if role == urole.role.name:
                    index = i
                    break
                    
            if index is None:
                # add it
                role_query = RoleModel.all()
                role_query.filter('name =', role)
                try:
                    new_role = role_query.fetch(query.count())[0]
                except IndexError:
                    return jsonify({'result':'failure', 'name':'main', 'errors': {}})
                new_urole = UserRoleModel(user=user.key(),
                                          role=new_role.key())
                new_urole.put()
            else:
                del uroles[index]
        for urole in uroles:
            urole.delete()

        user.save()
        
        return jsonify({'result':'success'})
    else:
        return jsonify({'result':'failure', 'name':'admin', 'errors': admin_form.errors})
    
@app.route('/members/edit/<cwruid>/contacts', methods=['GET', 'POST'])
@login_required
def display_edit_user_contact(cwruid):
    """
    This view allows the user and administrators
    to edit the contact information of that user
    """
    from flask.ext import wtf
    permissions = check_permissions(cwruid)
    if not permissions[0] and not permissions[1]:
        return permission_denied(cwruid)

    # get the user object and all associated objects
    try:
        user = find_users(1, cwruid=('=', cwruid))[0]
    except IndexError:
        return render_template('404.html'), 404


    # create blank forms
    emails_form = forms.EmailUpdateForm(None)
    addresses_form = forms.AddressUpdateForm(None)
    phones_form = forms.PhoneUpdateForm(None)

    # populate the form

    # get the emails
    query = models.EmailModel.all()
    query.filter('user =', user.key())
    emails = query.fetch(query.count())

    # create the email forms
    for i, email in enumerate(emails):
        emails_form.emails.append_entry(wtf.FormField(forms.EmailAddressForm()))
        emails_form.emails[i].key.data = str(email.key())
        if email.name is not None:
            emails_form.emails[i].emailName.data = email.name
        if email.email is not None:
            emails_form.emails[i].emailAddress.data = email.email

    if len(emails_form.emails) <= 0:
        emails_form.emails.append_entry(wtf.FormField(forms.EmailAddressForm()))


    # get the phone numbers
    query = models.PhoneModel.all()
    query.filter('user =', user.key())
    numbers = query.fetch(query.count())

    # create the phone numbers forms
    for i, number in enumerate(numbers):
        phones_form.phones.append_entry(wtf.FormField(forms.PhoneNumberForm()))
        phones_form.phones[i].key.data = str(number.key())
        if number.name is not None:
            phones_form.phones[i].phoneName.data = number.name
        if number.number is not None:
            phones_form.phones[i].phoneNumber.data = number.number

    if len(phones_form.phones) <= 0:
        phones_form.phones.append_entry(wtf.FormField(forms.PhoneNumberForm()))

    # get the address
    query = models.AddressModel.all()
    query.filter('user =', user.key())
    addresses = query.fetch(query.count())

    # create the address forms
    for i, address in enumerate(addresses):
        addresses_form.addresses.append_entry(wtf.FormField(forms.AddressForm()))
        addresses_form.addresses[i].key.data = str(address.key())
        if address.name is not None:
            addresses_form.addresses[i].addrName.data = address.name
        if address.street1 is not None:
            addresses_form.addresses[i].street1.data = address.street1
        if address.street2 is not None:
            addresses_form.addresses[i].street2.data = address.street2
        if address.city is not None:
            addresses_form.addresses[i].city.data = address.city
        if address.state is not None:
            addresses_form.addresses[i].state.data = address.state
        if address.zip_code is not None:
            addresses_form.addresses[i].zip_code.data = address.zip_code

    if len(addresses_form.addresses) <= 0:
        addresses_form.addresses.append_entry(wtf.FormField(forms.AddressForm()))
        
    # render the edit template
    return render_template('members/edit_contacts.html',
                           emails_form=emails_form,
                           phones_form=phones_form,
                           addresses_form=addresses_form,
                           current_user=current_user,
                           user=user)


@app.route('/members/edit/<cwruid>/contacts/emails/json', methods=['POST'])
@login_required
def handle_edit_contacts_emails_json(cwruid):
    """
    This method handles the submission
    of the EmailUpdateForm submitted from the
    display_edit_contacts view
    """
    permissions = check_permissions(cwruid)
    if not permissions[0] and not permissions[1]:
        return jsonify({'result':'failure', 'msg':'Permission denied'})

    emails_form = forms.EmailUpdateForm()
    
    if emails_form.validate():
        try:
            user = find_users(1, cwruid=('=', cwruid))[0]
        except IndexError:
            return jsonify({'result':'failure', 'name':'main', 'errors': {}})

        query = models.EmailModel.all()
        query.filter('user =', user.key())
        emails = query.fetch(query.count())
        for email_form in emails_form.emails:
            if email_form.key.data == '':
                # create new email
                name = email_form.emailName.data
                if name == '':
                    name = None
                email = models.EmailModel(user=user.key(),
                                          email=email_form.emailAddress.data,
                                          name=name)
                email.put()
            else:
                # try and see what email was updated
                index = None
                for i, email in enumerate(emails):
                    if str(email.key()) == email_form.key.data:
                        email.name = email_form.emailName.data
                        email.email = email_form.emailAddress.data
                        email.put()
                        index = i
                        break
                # remove from the list so that
                # only emails with no associated
                # forms get deleted at the end
                if index is not None:
                    del emails[index]
        for email in emails:
            email.delete()
    else:
        # process errors
        errors = {}
        for i, email_form in enumerate(emails_form.emails):
            for error in email_form.errors:
                errors['emails-%i-%s' % (i, error)] =  email_form[str(error)].errors
        return jsonify({'result':'failure', 'name':'emails', 'errors': errors})
    
    return jsonify({'result':'success'})

@app.route('/members/edit/<cwruid>/contacts/phones/json', methods=['POST'])
@login_required
def handle_edit_contacts_phones_json(cwruid):
    """
    This method handles the submission
    of the PhoneUpdateForm submitted from the
    display_edit_contacts view
    """
    permissions = check_permissions(cwruid)
    if not permissions[0] and not permissions[1]:
        return jsonify({'result':'failure', 'msg':'Permission denied'})

    try:
        user = find_users(1, cwruid=('=', cwruid))[0]
    except IndexError:
        return jsonify({'result':'failure', 'name':'main', 'errors': {}})
        
    phones_form = forms.PhoneUpdateForm()
        
    if phones_form.validate():
        query = models.PhoneModel.all()
        query.filter('user =', user.key())
        phones = query.fetch(query.count())
        flash(phones)
        for phone_form in phones_form.phones:
            name = phone_form.phoneName.data
            if name == '':
                name = None
            if phone_form.key.data == '':
                # create new phone
                phone = models.PhoneModel(user=user.key(),
                                          number=phone_form.phoneNumber.data,
                                          name=name)
                phone.put()
            else:
                # try and see what phone was updated
                index = None
                for i, phone in enumerate(phones):
                    if str(phone.key()) == phone_form.key.data:
                        phone.name = name
                        phone.number = phone_form.phoneNumber.data
                        phone.put()
                        index = i
                        break
                if index is not None:
                    del phones[index]
        for phone in phones:
            phone.delete()
    else:
        # process errors
        errors = {}
        for i, phone_form in enumerate(phones_form.phones):
            for error in phone_form.errors:
                errors['phones-%i-%s' % (i, error)] =  phone_form[str(error)].errors
        return jsonify({'result':'failure', 'name':'phones', 'errors': errors})
        
    return jsonify({'result':'success'})

@app.route('/members/edit/<cwruid>/contacts/addresses/json', methods=['POST'])
@login_required
def handle_edit_contacts_addresses_json(cwruid):
    """
    This method handles the submission of the
    AddressUpdateForm. It is submitted from the
    display_edit_contacts view
    """
    permissions = check_permissions(cwruid)
    if not permissions[0] and not permissions[1]:
        return jsonify({'result':'failure', 'msg':'Permission denied'})

    try:
        user = find_users(1, cwruid=('=', cwruid))[0]
    except IndexError:
        return jsonify({'result':'failure', 'name':'main', 'errors': {}})
        
    addresses_form = forms.AddressUpdateForm()
        
    if addresses_form.validate():
        query = models.AddressModel.all()
        query.filter('user =', user.key())
        addresses = query.fetch(query.count())
        for address_form in addresses_form.addresses:
            name = address_form.addrName.data
            if name == '':
                name = None
            street2 = address_form.street2.data
            if street2 == '':
                street2 = None
            if address_form.key.data == '':
                # create new address
                address = models.AddressModel(user=user.key(),
                                             street1=address_form.street1.data,
                                             street2=street2,
                                             city=address_form.city.data,
                                             state=address_form.state.data,
                                             zip_code=str(address_form.zip_code.data),
                                             name=name)
                address.put()
            else:
                # try and see what address was updated
                index = None
                for i, address in enumerate(addresses):
                    if str(address.key()) == address_form.key.data:
                        address.name = name
                        address.street1 = address_form.street1.data
                        address.city = address_form.city.data
                        address.state = address_form.state.data
                        address.zip_code = str(address_form.zip_code.data)
                        address.street2 = street2
                        address.put()
                        index = i
                        break
                if index is not None:
                    del addresses[index]
        for address in addresses:
            address.delete()
    else:
        errors = {}
        for i, address_form in enumerate(addresses_form.addresses):
            for error in address_form.errors:
                errors['addresses-%i-%s' % (i, error)] =  address_form[str(error)].errors
        return jsonify({'result':'failure', 'name':'addresses', 'errors': errors})
        
    return jsonify({'result':'success'})

@app.route('/members/edit/<cwruid>/profile', methods=['GET', 'POST'])
@login_required
def display_edit_user_profile(cwruid):
    """
    This view allows the user and administrators to
    edit the profile of that user
    """

    permissions = check_permissions(cwruid)
    if not permissions[0] and not permissions[1]:
        return jsonify({'result':'failure', 'msg':'Permission denied'})
    
    return "Not yet implemented!"