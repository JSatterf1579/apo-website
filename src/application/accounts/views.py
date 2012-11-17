"""This module contains the views for the accounts package

.. module:: application.accounts.views

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

from flaskext.flask_login import login_user, login_required, logout_user, current_user

import urlparse, urllib

from application import app

from flask import render_template, flash, url_for, redirect, request

from application.accounts import accounts, forms, models

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm(request.form)

    if request.method == 'POST' and form.validate():

        # get the User from the database based on cwruid
        cwruid = form.cwruid.data
        password = form.password.data

        users = accounts.find_users(cwruid=('=',cwruid))

        if(len(users) != 1):
            flash("Error: Something went wrong. Please contact the webmasters", 'error')
            params = '?'
            for key in request.args:
                params += '%s=%s' % (urllib.quote_plus(key), urllib.quote_plus(request.args[key]))
            return redirect(urlparse.urljoin(request.path, params)) # try again


        if users[0].valid_password(password):
            login_user(users[0])
            try:
                nextPage = request.args['next']
            except KeyError:
                nextPage = '/'
            flash('Success! You are now logged in', 'success')
            return redirect(urlparse.urljoin(request.host_url, nextPage))
        else:
            flash('Error: Incorrect username or password', 'error')
        

    try:
        next = urllib.quote_plus(request.args['next'])
    except KeyError:
        next = urllib.quote_plus('/')
    return render_template('accounts/login.html', loginForm=forms.LoginForm(), next=next)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.context_processor
def loginLink():
    if current_user.is_authenticated():
        return dict(loggedIn = True,
                    loginLink='<a href="/logout">Logout %s</a>' % current_user.cwruid)
    else:
        return dict(loginLink='<a href="/login">Login</a>')

@app.route('/resetpassword', methods=['GET', 'POST'])
def reset_password():
    """
    This view allows a user that has forgetten their password
    to request a new one via their case email account
    """
    return "Reset password page"