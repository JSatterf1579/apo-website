"""
This module contains the forms used by the contracts package
"""

from flaskext import wtf
from flaskext.wtf import validators

class ContractForm(wtf.Form):
    name = wtf.TextField('Contract Name*', [validators.Required()])
    desc = wtf.TextField('Description', [validators.Optional()])

class ReqForm(wtf.Form):
    name = wtf.TextField('Requirement Name', [validators.Required()])
    due_date = wtf.DateField('Due Date', [validators.Required()])

class TimeReqForm(ReqForm):
    hours = wtf.IntegerField('Required Time (hours)', [validators.Required()])

class DuesReqForm(ReqForm):
    amount = wtf.FloatField('Amount ($)', [validators.Required()])