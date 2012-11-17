"""This module contains the views for the members package.

.. module:: application.members.views

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

from flaskext.flask_login import current_user, login_required

from application import app

from application.accounts.accounts import require_roles, create_user, find_users
from application.accounts import accounts

import forms
import models
from members import get_family_names, get_role_names, send_new_user_mail

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

    # get the choices for the CreateUserForm family field
    family_names = get_family_names()

    family_choices = []
    for name in family_names:
        family_choices.append((name, name.title()))

    # get the choices for the CreateUserForm role field
    role_names = get_role_names()

    role_choices = []
    for name in role_names:
        role_choices.append((name, name.title()))
    
    form.family.choices = family_choices
    form.roles.choices = role_choices

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
            if form.family.data != '':
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
                accounts.create_user(fname, lname, cwruid, password)#, **optional_attr)
                flash('User created successfully', 'success')

                # check if this the test server
                # if it is the test server don't send an email
                import os
                if os.environ['SERVER_SOFTWARE'].startswith('Development'):
                    flash('Password: %s' % password)
                else:
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
    return "List Users Page"

@app.route('/members/delete/<cwruid>', methods=['GET'])
@login_required
@require_roles(names=['webmaster', 'membership'])
def delete_user(cwruid):
    """
    When this view receives a GET request, if the
    user has the correct role then the user will
    be deleted
    """
    return "Deleting %s" % cwruid

@app.route('/members/view/<cwruid>', methods=['GET'])
@login_required
def view_user(cwruid):
    """
    This view displays the profile information
    for the request cwruid
    """
    return "User profile for %s" % cwruid

@app.route('/members/edit/<cwruid>', methods=['GET'])
@login_required
def edit_user(cwruid):
    """
    This view allows the user and administrators
    to edit the profile of that user
    """
    return "Editing user profile for %s" % cwruid

