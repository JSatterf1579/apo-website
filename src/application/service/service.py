"""
This module contains the helper functions for the service package

.. module:: application.service.modules

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

from google.appengine.ext import db

from flaskext.flask_login import current_user
from flaskext import wtf

from flask import flash

import models, forms

import application.contracts.models as c_models

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

def create_service_report_review_form(event):
    """
    This method will create a service report reivew form
    using the data in the datastore.

    By default it creates the form for every hour report
    in the database. But if an event is specified then
    the form will only be for hour reports for that event
    """

    event_review = forms.ServiceReportReviewForm(None)

    event_review.event_id.data = event.key()

    query = models.InsideServiceReportModel.all()
    query.filter('event =', event.key())

    try:
        report = query.fetch(1)[0]
    except IndexError:
        return event_review


    for hour_report in report.servicehourmodel_set:
        event_review.hour_reviews.append_entry(wtf.FormField(forms.HourReviewForm(None)))
            
        hour_review = event_review.hour_reviews[-1]

        hour_review.status.data = hour_report.status
        hour_review.hour_report_id.data = hour_report.key()
        hour_review.user_name.data = hour_report.user.fname + " " + hour_report.user.lname
        if hour_report.hours is None:
            hour_review.hours.data = 0
        else:
            hour_review.hours.data = hour_report.hours
        if hour_report.minutes is None:
            hour_review.minutes.data = 0
        else:
            hour_review.minutes.data = hour_report.minutes
            
    return event_review
        
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

def update_contract_time_progress(hour_report, old_status, new_status):
    """
    Given the information in an hour report and the
    new status
    update the time requirement progress
    for the associated user accordingly
    """

    user = hour_report.user

    # how much to change the contract requirements by
    hours = hour_report.hours
    if hours == None:
        hours = 0

    minutes = hour_report.minutes
    if minutes == None:
        minutes = 0
    else:
        hours += minutes/60.0
        

    # find all of the relevant contract progresses
    req_progs = []

    for signed in user.signedcontractmodel_set:
        contract = signed.contract_
        for req in contract.reqmodel_set:
            if isinstance(req, c_models.TimeReqModel):
                for req_prog in req.timereqprogressmodel_set:
                    req_progs.append(req_prog)    

    for req_prog in req_progs:
        if (old_status == 'pending' or old_status == 'rejected') and new_status == 'approved':
            req_prog.time += hours
            req_prog.put()
            
        elif old_status == 'approved' and (new_status == 'rejected' or new_status == 'pending'):
            req_prog.time -= hours
            req_prog.put()

                        
