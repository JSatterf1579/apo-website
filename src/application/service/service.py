"""
This module contains the helper functions for the service package

.. module:: application.service.modules

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

from flaskext.flask_login import current_user
from flaskext import wtf

import models, forms

import urllib
import datetime as dt

def is_signed_up(event):
    """
    This method determines if the current
    user is signed up for the specified event.

    It returns the ServiceSignUpModel associated
    with the user, event pair if the user is signed up
    otherwise it returns None.
    """

    query = models.ServiceSignUpModel.all()
    query.filter('user =', current_user.key())
    query.filter('event =', event.key())

    try:
        return query.fetch(1)[0]
    except IndexError:
        return None

def prepare_service_event(event):
    """
    Takes in an event model and adds
    extra attributes so that the event
    can easily be manipulated
    in the templates
    """
    event.url_name = urllib.quote_plus(event.name)
    event.url_time = urllib.quote_plus(str(event.start_time))
    event.str_start_time = str(event.start_time)
    event.str_end_time = str(event.end_time)

    return event
        
def get_service_event(event_name, event_time):
    """
    Takes in a url encoded event name
    and event time and searches the Datastore
    for a matching entity.

    Returns the entity if it is found. Otherwise returns None
    """

    query = models.ServiceEventModel.all()
    str_timestamp = urllib.unquote_plus(event_time)
    timestamp = dt.datetime.strptime(str_timestamp, '%Y-%m-%d %H:%M:%S')
    query.filter('start_time =', timestamp)
    query.filter('name =', urllib.unquote_plus(event_name))

    try:
        return query.fetch(1)[0]
    except IndexError:
        return None

def get_signups(event):
    """
    This function takes in an event
    instance and returns all signups
    associated with it in a list
    """

    signups = []
    for signup in event.servicesignupmodel_set:
        signups.append(signup)

    return signups

def create_inside_service_report_form(event):
    """
    This method takes in an event
    and creates a new inside service report form
    with enough fields for every brother that was on the
    sign up list
    """

    form = forms.ServiceReportForm(None)

    signups = get_signups(event)
    for signup in signups:
        form.hour_reports.append_entry(wtf.FormField(forms.HourReportForm(None)))
        form.hour_reports[-1].fname.data = signup.user.fname
        form.hour_reports[-1].lname.data = signup.user.lname
        form.hour_reports[-1].cwruid.data = signup.user.cwruid
        form.hour_reports[-1].hours.data = 0
        form.hour_reports[-1].minutes.data = 0

    return form

def get_service_report(event):
    """
    If a service report for this event exists then it
    is returned. Otherwise None is returned
    """

    query = models.InsideServiceReportModel.all()

    query.filter('event =', event.key())

    try:
        return query.fetch(1)[0]
    except IndexError:
        return None