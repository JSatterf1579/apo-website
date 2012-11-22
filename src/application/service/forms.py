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
    cwruid = wtf.TextField('Case ID*', [validators.Required()])
    hours = wtf.IntegerField('Hours*', [validators.Optional()])
    minutes = wtf.IntegerField('Minutes*', [validators.Optional()])
    
class ServiceReportForm(wtf.Form):
    hour_reports = wtf.FieldList(wtf.FormField(HourReportForm))

class InsideServiceReportForm(ServiceReportForm):
    event = wtf.SelectField('Event Name', [validators.Required()])

class OutsideServiceReportForm(ServiceReportForm):
    event_name = wtf.TextField('Event Name*', [validators.Required()])
    location = wtf.TextField('Location', [validators.Required()])
    desc = wtf.TextField('Description', [validators.Required()])
    date = wtf.DateTimeField('Date and Time', [validators.Required()])