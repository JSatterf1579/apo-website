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

from flask import render_template, flash, url_for, redirect, request

from google.appengine.api import mail


@app.route('/members/create', methods=['GET', 'POST'])
@login_required
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

    users = find_users()
    return render_template('members/list.html',
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

    if current_user.cwruid == cwruid:
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
    

    return render_template('members/view.html',
                           show_edit_link=show_edit_link,
                           user=user,
                           minitial=minitial,
                           avatar=avatar,
                           family=user.family.name.title(),
                           big=user.big,
                           emails=emails,
                           numbers=numbers,
                           addresses=addresses)
                           
                           

@app.route('/members/edit/<cwruid>', methods=['GET', 'POST'])
@login_required
def edit_user(cwruid):
    """
    This view allows the user and administrators
    to edit the profile of that user
    """
    from flaskext import wtf
    
    import urlparse, urllib
    import json
    admin_roles = ['webmaster', 'membership']

    # see if user is admin
    admin = False
    query = UserRoleModel.all()
    query.filter('user =', current_user.key())
    uroles = query.fetch(query.count())
    for urole in uroles:
        if urole.role.name in admin_roles:
            admin = True
            break
    
    # determine if the user can edit this page
    if current_user.cwruid != cwruid and not admin:
        flash("You don't have permission to access this page", 'error')
        params = '?%s=%s' % ('next', urllib.quote_plus(url_for('edit_user', cwruid=cwruid)))
        return redirect(urlparse.urljoin(request.host_url, url_for('login')) + params)

    if current_user.cwruid == cwruid:
        change_pass_link = True
    else:
        change_pass_link = False

    # if the program has made it this far then the user has permissions to edit this user

    # get the user object and all associated objects
    try:
        user = find_users(1, cwruid=('=', cwruid))[0]
    except IndexError:
        return render_template('404.html'), 404


    # populate the form
    main_form = forms.MainUpdateUserForm(request.form)
    admin_form = forms.AdminUpdateUserForm(request.form)
    emails_form = forms.EmailUpdateForm(request.form)
    addresses_form = forms.AddressUpdateForm(request.form)
    phones_form = forms.PhoneUpdateForm(request.form)

    # set the choices
    admin_form.family.choices = get_family_choices()
    admin_form.roles.choices = get_role_choices()

    # process the data
    if request.method == 'POST':
        result = 'success'
        if 'emails' in request.args:
            if emails_form.validate():
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

                emails_form = forms.EmailUpdateForm(None)
        else:
            result = 'false'
            if 'json' in request.args:
                return json.dumps(result)
        if 'phones' in request.args and phones_form.validate():
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

            phones_form = forms.PhoneUpdateForm(None)
        else:
            result = 'false'
            if 'json' in request.args:
                return json.dumps(result)
            
        if 'addresses in request.args' and addresses_form.validate():
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
            # clear out the old address form
            addresses_form = forms.AddressUpdateForm(None)
        else:
            result = 'false'
            if 'json' in request.args:
                return json.dumps(result)

    if 'json' in request.args:
        return json.dumps(result)
                
    # populate the form
    main_form = forms.MainUpdateUserForm(None)
    admin_form = forms.AdminUpdateUserForm(None)

    # set the choices
    admin_form.family.choices = get_family_choices()
    admin_form.roles.choices = get_role_choices()



    main_form.fname.data = user.fname
    main_form.mname.data = user.mname
    main_form.lname.data = user.lname
    main_form.avatar.data = user.avatar

    admin_form.cwruid.data = user.cwruid
    if user.big is not None:
        admin_form.big.data = user.big.cwruid
    if user.family is not None:
        admin_form.family.data = user.family.name

    # get the roles
    query = UserRoleModel.all()
    query.filter('user =', user.key())
    uroles = query.fetch(query.count())
    selected_roles = []
    for urole in uroles:
        selected_roles.append(urole.role.name)

    admin_form.roles.data = selected_roles

    if len(emails_form.emails) <= 0:
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

    if len(phones_form.phones) <= 0:
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

    if len(addresses_form.addresses) <= 0:
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
        
    # if this is a post process the data

       # process data!!
    
    # see if change password link should be visible

    # render the edit template
    return render_template('members/edit.html',
                           emails_form=emails_form,
                           phones_form=phones_form,
                           addresses_form=addresses_form,
                           change_pass_link=change_pass_link,
                           show_admin=admin,
                           current_user=current_user,
                           user=user)

