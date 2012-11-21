"""This file contains the models for the accounts package

.. module:: application.accounts.models

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""
from google.appengine.ext import db

class UserModel(db.Model): # pylint: disable=R0904
    """
    Stores user information. Also provides the methods needed to Flask-Login.
    
    .. method:: User(firstName, lastName, cwruID, salt, hash[, middleName, contractType, family, big, avatar])

       Creates a new User entity

       :param firstName: User's first name
       :type firstName: unicode

       :param lastName: User's last name
       :type lastName: unicode

       :param cwruID: User's Case network ID.
       :type cwruID: unicode

       :param salt: A unique string (per user) used in password hashing
       :type salt: unicode

       :param hash: A hash of the user's password with the user's salt
       :type hash: unicode

       :param middleName: User's middle name
       :type middleName: unicode

       :param contractType: User's Contract type
       :type contractType: application.models.Contract

       :param family: User's family
       :type family: application.models.Family

       :param big: User's big
       :type big: application.models.User

       :param avatar: User's gravatar user name
       :type avatar: unicode
    """
    # Required attributes
    fname = db.StringProperty(required=True)
    lname = db.StringProperty(required=True)
    cwruid = db.StringProperty(required=True)
    salt = db.StringProperty(required=True)
    hash = db.StringProperty(required=True)

    # Optional attributes
    mname = db.StringProperty(default=None)
    # might want to enforce reference type on contractType and family
    contract_type = db.ReferenceProperty(default=None,
                                        collection_name='contract')
    family = db.ReferenceProperty(default=None,
                                  collection_name='family')
    big = db.SelfReferenceProperty(default=None, collection_name='littles')
    avatar = db.StringProperty(default=None)

class RoleModel(db.Model):
    
    # required attributes
    name = db.StringProperty(required=True)

    # optional attributes
    desc = db.StringProperty(required=True)

class UserRoleModel(db.Model):

    # required attributes
    user = db.ReferenceProperty(UserModel, required=True)
    role = db.ReferenceProperty(RoleModel, required=True)