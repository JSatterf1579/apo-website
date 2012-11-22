"""
This module contains the views for the service package

.. module:: application.service.views

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

from application import app

from flask import flash, render_template, redirect, url_for, jsonify, request
from flaskext.flask_login import current_user, login_required

import forms, models
from service import prepare_service_event, get_service_event, is_signed_up, get_signups

import datetime as dt

from application.members import members
from application.accounts.accounts import require_roles

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

    return render_template('service/show.html',
                           can_edit=members.can_edit(['webmaster']),
                           event=event,
                           signed_up=signed_up,
                           future=future,
                           full=full,
                           signups=signups,
                           num_signed_up=len(signups))

@app.route('/service/<event_name>/<event_time>/signup')
def service_event_signup(event_name, event_time):
    """
    This view will sign a user up for an event
    """

    event = get_service_event(event_name, event_time)
    event = prepare_service_event(event)

    signups = get_signups(event)

    if event.maxBro is not None and len(signups) < event.maxBro:
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
def service_event_unsignup(event_name, event_time):
    """
    This view will unsign a user up for an event
    """

    event = get_service_event(event_name, event_time)
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