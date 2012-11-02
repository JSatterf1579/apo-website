"""This module contains methods related to user accounts and logins.
Contained in the accounts package

.. module:: application.accounts.accounts

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""
import sys, os

sys.path.insert(0, os.path.abspath('../../'))

import flaskext.flask_login as login

from application.accounts.models import UserModel
from Crypto.Hash import SHA # used with the passwords
from application.generate_keys import generate_randomkey

class User(login.UserMixin):
    """This call is the main class used for accounts.
    It contains all of the information about a specific
    user that is in the datastore. This class is a wrapper
    around the user model

    This class should not be instantiated by anything other than
    the application.accounts.accounts.create_user and the
    application.accounts.accounts.find_users methods. This is
    to prevent security issues when dealing with passwords.
    It also enforces data integrity rules such as no two users
    can share the same cwruID"""

    # add more attribute names here to make them
    # nonmodifiable via __setattr__
    non_modifiable_attr = ['hash', 'salt']
    
    def __init__(self): # pylint: disable=W0231
        pass

    def __setattr__(self, name, value):
        if name in User.non_modifiable_attr:
            raise AttributeError('%s is nonmodifiable' % name)
        else:
            self.__dict__[name] = value

def create_user(fname, lname, cwruid, password, **kwargs):
    """This method is a factory method for User accounts.
    It takes in the required fields of fname, lname,
    and cwruid. It queries the database to make sure that the
    cwruid is unique. If it is not an AttributeError exception
    is raised with the message stating that the cwruid is not
    unique. It then generates a string of salt using the
    secure random number generator in the Crypto module. The
    provided password is then hashed with the salt. All of this
    information is added to an instance of a UserModel class
    from the application.accounts.models module.

    If any optional arguments are supplied through the kwargs
    dictionary they are checked against the attributes of the
    UserModel class. If the argument matches an attribute
    in the UserModel and the attribute is modifiable
    outside of the accounts module and the value is valid
    for that attribute it is added to the UserModel instance
    created during the initial steps. If these conditions are
    not met an AttributeError exception is raised with the
    message specifying the argument that caused the problem.

    Finally the entire UserModel instance is saved to the
    datastore via the UserModel's put method. This UserModel
    is then stored inside of a new instance of the
    application.accounts.accounts.User class.

    If everything was successful the User instance is
    returned. Otherwise None is returned
    """

    query = UserModel.all()
    query.filter('cwruid =', cwruid)

    # If there is already a user in the database
    # with the same cwruID
    if(query.count() > 0):
        raise AttributeError('CWRU ID %s already exists. ' % cwruid +
                             'CWRU ID must be unique')
    
    salt = generate_randomkey(256)
    hasher = SHA.new(salt + password)
    
    user_model = UserModel(fname=fname,
                          lname=lname,
                          cwruid=cwruid,
                          salt=salt,
                          hash=hasher.hexdigest())

    for key in kwargs:
        # the values in non_modifiable_attr
        # should not be modified by information
        # from outside of this function
        if key in User.non_modifiable_attr:
            raise AttributeError
        user_model.__setattr__(key, kwargs[key])

    user_model.put()

    new_user = User()
    new_user._User__UserModel = user_model # pylint: disable=C0103,W0201
    return new_user