"""This module contains methods related to user profiles
and permissions.

It utilizes the methods found in the accounts package.

.. module:: application.members.members

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

import urllib, hashlib, urlparse

from models import FamilyModel
from application.accounts.models import RoleModel, UserRoleModel

import urlparse, urllib

from flaskext.flask_login import current_user

from flask import render_template, url_for, redirect, flash, request

def get_avatar_url(email, host, size=100, default='/static/img/avatar.png'):
    """
    This function takes a Gravatar email address
    and returns the gravatar image url

    :param email: The Gravatar email address
    :type email: unicode

    :param size: Size of the returned avatar image
    :type size: int

    :param default: Default avatar url
    :type default: unicode
    """

    gravatar_url = "http://www.gravatar.com/avatar/"
    gravatar_url += hashlib.md5(email.lower()).hexdigest() + "?"
    gravatar_url += urllib.urlencode({'d':urlparse.urljoin(host,default)
                                      , 's':str(size)})

    return gravatar_url

def get_families():
    """
    Returns a list of all Family entities in the db
    """


    query = FamilyModel.all()

    count = query.count()

    return query.fetch(count)
    

def get_family_choices():
    """
    Returns the list of family names in the database
    """

    families = get_families()

    choices = []
    for family in families:
        choices.append((family.name, family.name.title()))

    choices.sort()

    choices.insert(0, ('none', 'None'))
    return choices

def get_roles():
    """
    Returns list of RoleModel Entities from the db
    """
    
    query = RoleModel.all()
    count = query.count()
    return query.fetch(count)
    
    
def get_role_choices():
    """
    Returns the list of role names in the database
    """
    roles = get_roles()
    
    choices = []
    for role in roles:
        choices.append((role.name, role.name.title()))
    
    return choices

def send_new_user_mail(fname, lname, cwruid, password):
    """
    Sends an account creation email to the user specified
    """
    from google.appengine.api import mail

    body = """
Hello %s,
   
Your new APO website account has been created.
You can visit http://apo-cwru.appspot.com/ and sign in using the following
username and password.

    username: %s
    password: %s

If you have any problems or questions please contact the webmasters at
webmaster@apo.case.edu

Thanks,

The APO Website
"""
    body %= (fname, cwruid, password)


    mail.send_mail(sender='APO Theta Upsilon Website <webmaster@apo.case.edu>',
                   to='%s %s <%s@case.edu>' % (fname, lname, cwruid),
                   subject='Your new account has been created',
                   body=body)

def check_permissions(cwruid):
    """
    Returns a permissions tuple.

    The first element in the tuple is whether the current
    account is the account being accessed.

    The second element in the tuple is whether the current
    user is a webmaster
    """

    # see if the user is the current user
    same_user = False
    if current_user.cwruid == cwruid:
        same_user = True

    # see if the user is an admin
    admin_user = False

    query = UserRoleModel.all()
    query.filter('user =', current_user.key())
    uroles = query.fetch(query.count())
    for urole in uroles:
        if urole.role.name == 'webmaster':
            admin_user = True
            break

    return (same_user, admin_user)

def permission_denied(cwruid):
    """
    If the user does not have the permissions required by the page
    then the user is redirected to the login page
    with a message stating that they do not have the permissions
    """
    import urllib, urlparse

    flash("You don't have permssion to access this page", 'error')
    params = '?%s=%s' % ('next', urllib.quote_plus(url_for('display_edit_user_account', cwruid=cwruid)))
    return redirect(urlparse.urljoin(request.host_url, url_for('login'))+params)
