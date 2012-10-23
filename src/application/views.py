"""URL Route Handlers

.. module:: application.views
   :synopsis: URL Route Handlers

.. moduleauthor:: Devin Schwab <dts34@case.edu>
.. moduleauthor:: Jon Chan <jtc77@case.edu>
"""


from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from flask import render_template, flash, url_for, redirect

from models import ExampleModel
from decorators import login_required, admin_required
from forms import ExampleForm

# this allows the use of the URL decorators
from application import app

@app.route('/')
def home():
    """
    View for the homepage

    :rtype: HTML page
    """
    return redirect(url_for('list_examples'))


@app.route('/hello/<username>')
def say_hello(username):
    """Contrived example to demonstrate Flask's url routing capabilities"""
    return 'Hello %s' % username


@app.route('/examples', methods=['GET','POST'])
@login_required
def list_examples():
    """List all examples"""
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