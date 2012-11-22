"""
This module contains the views for the service package

.. module:: application.service.views

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

from application import app

from flask import flash, render_template, redirect, url_for, jsonify, request
from flaskext.flask_login import current_user, login_required

import forms, models

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
        event.url_name = urllib.quote_plus(event.name)
        event.url_time = urllib.quote_plus(str(event.start_time))
        event.str_start_time = str(event.start_time)
        event.str_end_time = str(event.end_time)

    query = models.ServiceEventModel.all()
    query.filter('start_time <=', now)
    query.order('-start_time')

    past_events = query.fetch(query.count())
    for event in past_events:
        event.url_name = urllib.quote_plus(event.name)
        event.url_time = urllib.quote_plus(str(event.start_time))
        event.str_start_time = str(event.start_time)
        event.str_end_time = str(event.end_time)

    
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

    return "TO DO"