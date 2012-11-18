"""This module contains the forms for the members package

.. module:: application.members.forms

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

from flaskext import wtf
from flaskext.wtf import validators

class AddressForm(wtf.Form):
    addrName = wtf.TextField('Name', [validators.Optional()])
    street1 = wtf.TextField('Street', [validators.Optional()])
    street2 = wtf.TextField('', [validators.Optional()])
    city = wtf.TextField('City', [validators.Optional()])
    state = wtf.TextField('State', [validators.Optional()])
    zip_code = wtf.IntegerField('Zip', [validators.Optional()])
    key = wtf.HiddenField([validators.Optional()])
    delete = wtf.SubmitField('Delete', [validators.Optional()])

class PhoneNumberForm(wtf.Form):
    phoneName = wtf.TextField('Name', [validators.Optional()])
    phoneNumber = wtf.TextField('Phone Number', [validators.Optional()])
    key = wtf.HiddenField([validators.Optional()])
    delete = wtf.SubmitField('Delete', [validators.Optional()])

class EmailAddressForm(wtf.Form):
    emailName = wtf.TextField('Name', [validators.Optional()])
    emailAddress = wtf.TextField('Email', [validators.Optional()])
    key = wtf.HiddenField([validators.Optional()])
    delete = wtf.SubmitField('Delete', [validators.Optional()])

class UpdateUserAdminForm(wtf.Form):
    cwruid = wtf.TextField('CWRU ID*', [validators.Required()])
    big = wtf.TextField('Big CWRU ID', [validators.Optional()])
    family = wtf.SelectField('Family', [validators.Optional()])
    roles = wtf.SelectMultipleField('Roles', [validators.Optional()])    

    
class UpdateUserForm(wtf.Form):
    fname = wtf.TextField('First Name*', [validators.Required()])
    mname = wtf.TextField('Middle Name', [validators.Optional()])
    lname = wtf.TextField('Last Name*', [validators.Required()])
    avatar = wtf.TextField('Gravatar Email', [validators.Optional(),
                                              validators.Email()])
    admin_form = wtf.FormField(UpdateUserAdminForm)
    addresses = wtf.FieldList(wtf.FormField(AddressForm))
    phone_numbers = wtf.FieldList(wtf.FormField(PhoneNumberForm))
    emails = wtf.FieldList(wtf.FormField(EmailAddressForm))
    update = wtf.SubmitField('Update', [validators.Optional()])

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


