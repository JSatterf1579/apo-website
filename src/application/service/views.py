"""
This module contains the views for the service package

.. module:: application.service.views

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

from google.appengine.ext import db, ndb

from application import app

from flask import flash, render_template, redirect, url_for, jsonify, request
from flaskext.flask_login import current_user, login_required

import forms, models
from service import prepare_service_event, get_service_event, is_signed_up
from service import get_signups, create_inside_service_report_form, get_service_report
from service import create_service_report_review_form, update_contract_time_progress

import datetime as dt

from application.members import members
from application.accounts.accounts import require_roles, find_users

import urllib

@app.route('/service')
@login_required
def service_list():
    """
    This view lists all service events that
    are in the future with the nearest in time
    appearing first.

    It also lists old service events at the bottom
    """

    can_edit = members.can_edit(['webmaster'])

    now = dt.datetime.now()
    
    query = models.ServiceEventModel.all()
    query.filter('start_time >', now)
    query.order('start_time')

    future_events = query.fetch(query.count())
    for event in future_events:
        event = prepare_service_event(event)
        

    query = models.ServiceEventModel.all()
    query.filter('start_time <=', now)
    query.order('-start_time')

    past_events = query.fetch(query.count())
    for event in past_events:
        event = prepare_service_event(event)

    
    return render_template('service/list.html',
                           can_edit=can_edit,
                           future_events=future_events,
                           past_events = past_events)

@app.route('/service/create', methods=['GET', 'POST'])
@require_roles(names=['webmaster'])
def service_create_event():
    """
    This view creates a new service event
    """

    form = forms.CreateServiceEventForm()

    if request.method == 'POST' and form.validate():
        desc = None
        if form.desc.data != '':
            desc = form.desc.data
        max_bros = None
        if form.max_bros.data != '':
            max_bros = form.max_bros.data
        addinfo = None
        if form.addinfo.data != '':
            addinfo = form.addinfo.data
        event = models.ServiceEventModel(name=form.name.data,
                                         description=desc,
                                         start_time=form.start_time.data,
                                         end_time=form.end_time.data,
                                         location=form.location.data,
                                         maxBro=max_bros,
                                         addInfo=addinfo)
        event.put()

        return redirect(url_for('service_show_event',
                                event_name=urllib.quote_plus(event.name),
                                event_time=urllib.quote_plus(str(event.start_time))))
                                         
    return render_template('service/create.html',
                           form=form)
    
@app.route('/service/<event_name>/<event_time>')
@login_required
def service_show_event(event_name, event_time):
    """
    This view displays a single service event
    and allows a user to sign up if there are spots avaiable
    """

    event = get_service_event(event_name, event_time)

    if event is None:
        return render_template('404.html'), 404
    
    event = prepare_service_event(event)
    
    signed_up = is_signed_up(event)

    signups = get_signups(event)

    full = None
    if event.maxBro is not None and len(signups) >= event.maxBro:
        full = True

    future = None
    if event.start_time > dt.datetime.now():
        future = True

    service_report = get_service_report(event)

    return render_template('service/show.html',
                           can_edit=members.can_edit(['webmaster']),
                           event=event,
                           signed_up=signed_up,
                           future=future,
                           full=full,
                           signups=signups,
                           service_report=service_report,
                           num_signed_up=len(signups))

@app.route('/service/<event_name>/<event_time>/signup')
@login_required
def service_event_signup(event_name, event_time):
    """
    This view will sign a user up for an event
    """

    event = get_service_event(event_name, event_time)
    if event is None:
        return render_template('404.html'), 404
    event = prepare_service_event(event)

    signups = get_signups(event)

    if (event.maxBro is not None and len(signups) < event.maxBro) or event.maxBro is None:
        signup = models.ServiceSignUpModel(user=current_user.key(),
                                           event=event.key())
        signup.put()

        flash('Successfully signup up for event', 'success')
    else:
        flash('Error signing up for event. Event is already full', 'error')
    return redirect(url_for('service_show_event',
                            event_name=event.url_name,
                            event_time=event.url_time))

@app.route('/service/<event_name>/<event_time>/unsignup')
@login_required
def service_event_unsignup(event_name, event_time):
    """
    This view will unsign a user up for an event
    """

    event = get_service_event(event_name, event_time)
    if event is None:
        return render_template('404.html'), 404
    event = prepare_service_event(event)

    signup = is_signed_up(event)

    if signup is not None:
        signup.delete()

        flash('Successfully removed from event', 'success')
    else:
        flash('Error removing you from event. Please try again', 'error')
    return redirect(url_for('service_show_event',
                            event_name=event.url_name,
                            event_time=event.url_time))

@app.route('/service/<event_name>/<event_time>/delete')
@require_roles(names=['webmaster'])
def service_delete_event(event_name, event_time):
    """
    This view deletes the specified
    service event and all related
    signups
    """

    event = get_service_event(event_name, event_time)

    if event is None:
        return render_template('404.html'), 404

    signups = get_signups(event)

    for signup in signups:
        signup.delete()

    event.delete()
    return redirect(url_for('service_list'))

@app.route('/service/<event_name>/<event_time>/edit', methods=['GET','POST'])
@require_roles(names=['webmaster'])
def service_edit_event(event_name, event_time):
    """
    This view allows a service event to be edited
    """

    event = get_service_event(event_name, event_time)
    if event is None:
        return render_template('404.html'), 404

    event = prepare_service_event(event)
    
    form = forms.CreateServiceEventForm()
    if request.method == 'POST':
        if form.validate():
            event.name = event.name
            if form.desc.data != '':
                event.description = form.desc.data
            else:
                event.description = None
            event.start_time = form.start_time.data
            event.end_time = form.end_time.data
            event.location = form.location.data
            if form.addinfo.data != '':
                event.addInfo = form.addinfo.data
            else:
                event.addInfo = None
            event.maxBro = form.max_bros.data

            event.put()

            # time has changed so have to reprepare
            event = prepare_service_event(event)

            return redirect(url_for('service_show_event',
                                    event_name=event.url_name,
                                    event_time=event.url_time))
    else:
        form.name.data = event.name
        form.desc.data = event.description
        form.start_time.data = event.start_time
        form.end_time.data = event.end_time
        form.location.data = event.location
        form.addinfo.data = event.addInfo
        form.max_bros.data = event.maxBro

    return render_template('service/create.html',
                           edit=True,
                           event=event,
                           form=form)

@app.route('/service/<event_name>/<event_time>/service-report', methods=['GET', 'POST'])
@login_required
def service_inside_report(event_name, event_time):
    """
    This view displays and processes
    inside service reports for the event
    specified by the url
    """

    event = get_service_event(event_name, event_time)
    if event is None:
        return render_template('404.html'), 404
        
    event = prepare_service_event(event)
    
    if request.method == 'POST':
        form = forms.ServiceReportForm()
        if form.validate():
            new_report = models.InsideServiceReportModel(event=event)
            new_report.put()

            # now create the associated hour reports
            for hour_report in form.hour_reports:
                try:
                    user = find_users(cwruid=('=', hour_report.cwruid.data))[0]
                except IndexError:
                    continue # this user doesn't exist so skip it

                hours = None
                if hour_report.hours.data > 0: # filter bad hours data
                    hours = hour_report.hours.data

                minutes = None
                if hour_report.minutes.data > 0: # filter bad minutes data
                    minutes = hour_report.minutes.data

                if hours is None and minutes is None:
                    continue # bad data so skip

                new_hour = models.ServiceHourModel(user=user.key(),
                                                   report=new_report.key(),
                                                   hours=hours,
                                                   minutes=minutes)
                new_hour.put()

                return redirect(url_for('service_show_event',
                                        event_name=event.url_name,
                                        event_time=event.url_time))
        else:
            flash(form.errors,'error')
    else:
        form = create_inside_service_report_form(event)

    return render_template('service/submit_inside_report.html',
                           form=form,
                           event=event)

@app.route('/service/report/<event_name>/<event_time>', methods=['GET', 'POST'])
@login_required
def service_report_status(event_name, event_time):
    """
    This view displays and processes hour report statuses
    """

    event = get_service_event(event_name, event_time)
    if event is None:
        return render_template('404.html'), 404

    event = prepare_service_event(event)

    can_edit = members.can_edit(['webmaster'])

    if request.method == 'POST' and can_edit is not None:
        form = forms.ServiceReportReviewForm()
        if form.validate():
            for hour_review in form.hour_reviews:
                
                query = models.ServiceHourModel.all()
                reports = query.fetch(query.count())

                for report in reports:
                    if str(report.key()) == hour_review.hour_report_id.data:
                        new_status = hour_review.status.data
                        old_status = report.status
                        report.status = new_status
                        report.put()
                        update_contract_time_progress(report, old_status, new_status)
                        break
                        
            return render_template('service/show_report.html',
                                   can_edit=can_edit,
                                   event=event,
                                   event_review=form)
        else:
            flash(form.errors)
    else:
        form = create_service_report_review_form(event=event)

    return render_template('service/show_report.html',
                           can_edit=can_edit,
                           event=event,
                           event_review=form)