"""URL Route Handlers

.. module:: application.views
   :synopsis: URL Route Handlers

.. moduleauthor:: Devin Schwab <dts34@case.edu>
.. moduleauthor:: Jon Chan <jtc77@case.edu>
"""


from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from flask import render_template, flash, url_for, redirect, request

from models import ExampleModel
from decorators import login_required, admin_required
from forms import ExampleForm

import models, forms, accounts, generate_keys

from flaskext.flask_login import login_user, login_required, logout_user, current_user

import urllib, urlparse

# this allows the use of the URL decorators and flask-login
from application import app

@app.before_first_request
def before_first_request():
    accounts.createUser(firstName='Devin',
                        lastName='Schwab',
                        cwruID='dts34',
                        password='default')
    accounts.createUser(firstName='Jon',
                        lastName='Chan',
                        cwruID='jtc77',
                        password='default')

@app.context_processor
def loginLink():
    if current_user.is_authenticated():
        return dict(loggedIn = True,
                    loginLink='<a href="/logout">Logout %s</a>' % current_user.cwruID)
    else:
        return dict(loginLink='<a href="/login">Login</a>')

@app.route('/')
def home():
    """
    View for the homepage

    :rtype: HTML page
    """
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    View for the login page
    """
    form = forms.LogInForm(request.form)

    if request.method == 'POST' and form.validate():

        # get the User from the database based on the username
        cwruID = form.username.data
        password = form.password.data
        
        if accounts.verifyLogin(cwruID, password):
            user = accounts.getUsers(limit=1,cwruID=cwruID)[0]
            login_user(user)

            try:
                nextPage = request.args['next']
            except KeyError:
                nextPage = 'home'
            flash('Success! You are now logged.', 'success')
            return redirect(urlparse.urljoin(request.host_url, nextPage))

        else:
            flash("Error: Incorrect username or password", 'error')
            params = '?'
            for key in request.args:
                params = params + '%s=%s' % (urllib.quote_plus(key),urllib.quote_plus(request.args[key]))
            return redirect(urlparse.urljoin(request.path, params)) # try again
    else:
        try:
            next = urllib.quote_plus(request.args['next'])
        except KeyError:
            next = urllib.quote_plus('/')
        return render_template('login.html', loginForm=forms.LogInForm(), next=next)

@app.route('/exec/members/create', methods=['GET', 'POST'])
@login_required
def createUser():
    """
    View for creating a user
    """

    form = forms.CreateUpdateProfileForm(request.form)
    
    if request.method == 'POST' and form.validate():
        if form.password.data == '':
            password = generate_keys.generate_randomkey(10)
        else:
            password = form.password.data
        newUser = accounts.createUser(form.fname.data,
                                      form.lname.data,
                                      form.caseid.data,
                                      password)
        if newUser is not None:
            flash("User '%s' created with password '%s'" % (newUser.cwruID,password))
            if(not current_user.is_authenticated):
                login_user(newUser)
        else:
            flash("Error: User was not created")
        return redirect(url_for('createUser'))
        
    return render_template('createUser.html', userForm=forms.CreateUpdateProfileForm())

@app.route('/exec/members')
@login_required
def listUsers():
    """
    View for listing users
    """

    users = accounts.getUsers()
    return render_template('listMembers.html', users=users)

@app.route('/exec/members/delete/<cwruID>')
@login_required
def deleteUser(cwruID):
    """
    View for deleting the user specified by cwruID
    """

    nextPage = 'listUsers'
    if current_user.cwruID == cwruID:
        logout_user()
        nextPage = 'home'

    success = accounts.deleteUser(cwruID)

    if(success):
        flash("Successfully deleted account '%s'" % cwruID)
    else:
        flash("Failed to delete account '%s'" % cwruID)
    return redirect(url_for(nextPage))

@app.route('/members/<cwruID>')
def viewUser(cwruID):
    """
    View for viewing the user's profile
    """

    return "Member profile for %s would display here" % cwruID

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/hello/<username>')
def say_hello(username):
    """Contrived example to demonstrate Flask's url routing capabilities

    :rtype: HTML page
    """
    return 'Hello %s' % username


@app.route('/examples', methods=['GET','POST'])
@login_required
def list_examples():
    """List all examples

    :rtype: HTML page
    """
    examples = ExampleModel.all()
    form = ExampleForm()
    if form.validate_on_submit():
        example = ExampleModel(
            example_name = form.example_name.data,
            example_description = form.example_description.data,
            added_by = users.get_current_user()
        )
        try:
            example.put()
            example_id = example.key().id()
            flash(u'Example %s successfully saved.' % example_id, 'success')
            return redirect(url_for('list_examples'))
        except CapabilityDisabledError:
            flash(u'App Engine Datastore is currently in read-only mode.', 'info')
            return redirect(url_for('list_examples'))
    return render_template('list_examples.html', examples=examples, form=form)


@app.route('/examples/delete/<int:example_id>', methods=['POST'])
@login_required
def delete_example(example_id):
    """Delete an example object"""
    example = ExampleModel.get_by_id(example_id)
    try:
        example.delete()
        flash(u'Example %s successfully deleted.' % example_id, 'success')
        return redirect(url_for('list_examples'))
    except CapabilityDisabledError:
        flash(u'App Engine Datastore is currently in read-only mode.', 'info')
        return redirect(url_for('list_examples'))


@app.route('/admin_only')
@admin_required
def admin_only():
    """This view requires an admin account"""
    return 'Super-seekrit admin page.'


def warmup():
    """App Engine warmup handler
    See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests

    """
    return ''

## Error handlers
# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500