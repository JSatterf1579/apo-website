"""
This module contains forms for the facebook integration module

.. module:: application.facebook.forms

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

from flaskext import wtf
from flaskext.wtf import validators

class AccessTokenOptionsForm(wtf.Form):
    use_albums = wtf.BooleanField('Use Albums', [validators.Optional()])
    token_key = wtf.HiddenField('Token Key', [validators.Optional()])

class MultiAccessTokenOptionsForm(wtf.Form):
    user_options = wtf.FieldList(wtf.FormField(AccessTokenOptionsForm))
    page_options = wtf.FieldList(wtf.FormField(AccessTokenOptionsForm))
