"""This module contains the forms for the members package

.. module:: application.members.forms

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

from flaskext import wtf
from flaskext.wtf import validators

class AddressForm(wtf.Form):
    addrName = wtf.TextField('Name', [validators.Optional()])
    street1 = wtf.TextField('Street', [validators.Required()])
    street2 = wtf.TextField('', [validators.Optional()])
    city = wtf.TextField('City', [validators.Required()])
    state = wtf.TextField('State', [validators.Required()])
    zip = wtf.IntegerField('Zip', [validators.Required()])

class PhoneNumberForm(wtf.Form):
    phoneName = wtf.TextField('Name', [validators.Optional()])
    phoneNumber = wtf.TextField('Phone Number', [validators.Required()])

class EmailAddressForm(wtf.Form):
    emailName = wtf.TextField('Name', [validators.Optional()])
    emailAddress = wtf.TextField('Email', [validators.Email()])

class SearchUserForm(wtf.Form):
    fname = wtf.TextField('First Name', [validators.Optional()])
    mname = wtf.TextField('Middle Name', [validators.Optional()])
    lname = wtf.TextField('Last Name', [validators.Optional()])

class CreateUserForm(wtf.Form):
    fname = wtf.TextField('First Name*', [validators.Required()])
    mname = wtf.TextField('Middle Name', [validators.Optional()])
    lname = wtf.TextField('Last Name*', [validators.Required()])
    cwruid = wtf.TextField('CWRU ID*', [validators.Required()])
    family = wtf.SelectField('Family', [validators.Optional()])
    big = wtf.TextField('Big CWRU ID', [validators.Optional()])
    avatar = wtf.TextField('Gravatar email', [validators.Email(), validators.Optional()])
    # need to make the role list change according to the roles in the database
    roles = wtf.SelectMultipleField('Role Name', [validators.Optional()])


