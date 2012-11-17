"""The file contains the models for the members package

.. module:: application.members.models

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""


from google.appengine.ext import db
from application.accounts.models import UserModel


class AddressModel(db.Model):
    """
    Contains an address for a User

    .. method:: AddressModel(user, address[, name])

       Creates a new AddressModel Entity

       :param user: User this address belongs to
       :type user: application.accounts.models.User

       :param address: Address
       :type address: google.appengine.ext.db.PostalAddress

       :param name: Nickname for Address - e.g. home
       :type name: unicode
    """

    # Required attributes
    user = db.ReferenceProperty(UserModel, required=True)
    address = db.PostalAddressProperty(required=True)

    # Optional attributes
    name = db.StringProperty()

class EmailModel(db.Model):
    """
    Contains an email address for a User

    .. method:: EmailModel(user, email[, name])

       Creates a new EmailModel Entity

       :param user: User this email belongs to
       :type user: application.accounts.models.User

       :param email: Email Address
       :type address: google.appengine.ext.db.Email

       :param name: Nickname for email address - e.g. school
       :type name: unicode
    """

    # Required attributes
    user = db.ReferenceProperty(UserModel, required=True)
    email = db.EmailProperty(required=True)

    # Optional attributes
    name = db.StringProperty()

class PhoneModel(db.Model):
    """
    Contains a Phone number for a User

    .. method:: PhoneModel(user, number[, name])

       Create a new PhoneModel Entity

       :param user: User this phone number belongs to
       :type user: application.accounts.models.User

       :param number: Phone Number
       :type number: google.appengine.ext.db.PhoneNumber

       :param name: Nickname for phone number - e.g. Cell
       :type name: unicode
    """

    # Required attributes
    user = db.ReferenceProperty(UserModel, required=True)
    email = db.PhoneNumberProperty(required=True)

    #Optional attributes
    name = db.StringProperty()

class FamilyModel(db.Model):
    """
    Contains the various families

    .. method:: FamilyModel(name)

       Creates a new FamilyModel entity

       :param name: Name of the family - e.g. Boehms
       :type name: unicode
    """
    name = db.StringProperty(required=True)