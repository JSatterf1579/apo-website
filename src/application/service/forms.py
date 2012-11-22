"""
This module contains the forms for the service package

.. module:: application.service.forms

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

from flaskext import wtf
from flaskext.wtf import validators

class CreateServiceEventForm(wtf.Form):
    name = wtf.TextField('Name*', [validators.Required()])
    desc = wtf.TextField('Description', [validators.Optional()])
    start_time = wtf.DateTimeField('Start Time*', [validators.Required()])
    end_time = wtf.DateTimeField('End Time*', [validators.Required()])
    location = wtf.TextField('Location*', [validators.Required()])
    addinfo = wtf.TextField('Additional Info', [validators.Optional()])
    max_bros = wtf.IntegerField('Maximum Number of Brothers', [validators.Optional()])

class HourReportForm(wtf.Form):
    fname = wtf.HiddenField('First Name', [validators.Optional()])
    lname = wtf.HiddenField('Last Name', [validators.Optional()])
    cwruid = wtf.HiddenField('Case ID*', [validators.Required()])
    hours = wtf.IntegerField('Hours*', [validators.Optional()])
    minutes = wtf.IntegerField('Minutes*', [validators.Optional()])
    
class ServiceReportForm(wtf.Form):
    hour_reports = wtf.FieldList(wtf.FormField(HourReportForm))

class OutsideServiceReportForm(ServiceReportForm):
    event_name = wtf.TextField('Event Name*', [validators.Required()])
    location = wtf.TextField('Location', [validators.Required()])
    desc = wtf.TextField('Description', [validators.Required()])
    date = wtf.DateTimeField('Date and Time', [validators.Required()])

class HourReviewForm(wtf.Form):
    status = wtf.RadioField('Status', [validators.Required()],
                            choices=[('approved', 'Approved'),
                                     ('rejected', 'Rejected'),
                                     ('pending', 'Pending')])
    hour_report_id = wtf.HiddenField('Hour Report ID', [validators.Required()])
    user_name = wtf.HiddenField('Name', [validators.Optional()])
    hours = wtf.HiddenField('Hours', [validators.Optional()])
    minutes = wtf.HiddenField('Minutes', [validators.Optional()])

class ServiceReportReviewForm(wtf.Form):
    hour_reviews = wtf.FieldList(wtf.FormField(HourReviewForm))
    event_id = wtf.HiddenField('Event ID', [validators.Required()])

