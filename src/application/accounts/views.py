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
    from application.generate_keys import generate_randomkey
    from google.appengine.api import mail
    
    form = forms.ResetPasswordForm(request.form)

    if request.method == 'POST' and form.validate():
        try:
            user = accounts.find_users(1, cwruid=('=', form.cwruid.data))[0]

            new_password = generate_randomkey(16)

            user.set_new_password(new_password)

            body = """
Hi %s,

Somebody requested a new password for you. You can now use

%s

when logging in.  If you did not request this password change
please contact the webmasters immediately.

Thanks,
The APO Website
"""
            body %= (user.fname, new_password)
            
            mail.send_mail(sender="APO Website <digidevin@gmail.com>",
                           to="%s %s <%s@case.edu>" % (user.fname, user.lname, user.cwruid),
                           subject='Your new password',
                           body=body)
            
        except IndexError:
            pass

        flash('If an account with the specified cwru id exists then it should\
              receive an email with a new password shortly', 'success')

        form = forms.ResetPasswordForm()
        
    return render_template('accounts/reset_password.html',
                            reset_password_form=form)

@app.route('/changepassword', methods=['GET', 'POST'])
@login_required
def update_password():
    """
    This view allows a user to reset their password.
    A user also is forced to visit this page
    when logging in for the first time or when
    logging in after their password has been reset
    """

    form = forms.ChangePasswordForm(request.form)

    if request.method == 'POST' and form.validate():
        if current_user.valid_password(form.old_password.data):
            current_user.set_new_password(form.new_password.data)

            return redirect(url_for('display_edit_user_account', cwruid=current_user.cwruid))
        else:
            form.old_password.errors.append(u'Incorrect password')

    return render_template('accounts/change_password.html',
                           change_password_form=form)