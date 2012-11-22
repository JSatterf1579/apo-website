"""URL Route Handlers

.. module:: application.views
   :synopsis: URL Route Handlers

.. moduleauthor:: Devin Schwab <dts34@case.edu>
.. moduleauthor:: Jon Chan <jtc77@case.edu>
"""


from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from flask import render_template, flash, url_for, redirect, request

from decorators import login_required, admin_required


import models, forms, accounts, generate_keys

from flaskext.flask_login import login_user, login_required, logout_user, current_user

import urllib, urlparse

# this allows the use of the URL decorators and flask-login
from application import app

from accounts.accounts import require_roles

@app.route('/')
def home():
    """
    Homepage
    """
    return redirect(url_for('display_blog'))

@app.route('/calendar')
def calendar():
    """
    View for the calendar
    """
    return render_template('calendar/calendar.html')

## Error handlers
# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500