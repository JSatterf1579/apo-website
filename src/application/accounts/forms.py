"""This module contains the forms for the accounts package

.. module:: application.accounts.forms

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

from flaskext import wtf
from flaskext.wtf import validators

class LoginForm(wtf.Form):

    cwruid = wtf.TextField('Name', [validators.Required()])
    password = wtf.PasswordField('Password: ', [validators.Required()])

class ChangePasswordForm(wtf.Form):

    old_password = wtf.PasswordField('Old Password: ', [validators.Required()])
    new_password = wtf.PasswordField('New Password: ', [validators.Required()])
    confirm_password = wtf.PasswordField('Confirm New Password: ',
                                         [validators.Required(),
                                          validators.EqualTo('new_password',
                                                             message='Passwords must match!')])

class ResetPasswordForm(wtf.Form):
    cwruid = wtf.TextField('CWRU ID: ', [validators.Required()])