"""
This module contains the views associated with the Facebook
administration.

For example in order to use many of the facebook integrated
features of the website, the website must have access to a valid
facebook account that has access to the desired objects.

The views in this module will allow the administrators of the website to
update the facebook accounts associated with the site.

.. module:: application.facebook.views

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

from flaskext.flask_login import current_user, login_required

from application import app

from flask import render_template, flash, url_for, redirect, request, make_response

import json, urlparse, urllib

import datetime as dt

import models

from application.accounts.accounts import require_roles

from google.appengine.api import urlfetch

from secret_keys import FACEBOOK_APP_ID, FACEBOOK_APP_SECRET
from application.generate_keys import generate_randomkey

@app.route('/facebook/admin')
@require_roles(names=['webmaster'])
def fb_admin_main():
    """
    UI for managing facebook related settings
    """
    
    query = models.AccessTokenModel.all()

    tokens = query.fetch(query.count())

    for token in tokens:
        token.time_left = str(token.expiration - dt.datetime.now())
        
    return render_template('facebook/admin.html',
                           tokens=tokens)

@app.route('/facebook/admin/delete-user-access/<username>')
@require_roles(names=['webmaster'])
def fb_admin_del_user_access(username):
    """
    Removes all tokens for a given user from the datastore
    """
    query = models.AccessTokenModel.all()
    query.filter('username =', username)

    tokens = query.fetch(query.count())

    for token in tokens:
        token.delete()

    return redirect(url_for('fb_admin_main'))

@app.route('/facebook/admin/get-user-access')
@require_roles(names=['webmaster'])
def fb_admin_get_user_access():
    """
    Main admin view for Facebook settings
    """

    login_url = 'https://www.facebook.com/dialog/oauth'
    access_url = 'https://graph.facebook.com/oauth/access_token'

    if 'code' not in request.args:
        login_params = {}
        login_params['client_id'] = FACEBOOK_APP_ID
        login_params['redirect_uri'] = request.base_url
        login_params['state'] = generate_randomkey(32)
        login_params['scope'] = 'user_birthday,read_stream'

        resp = make_response(redirect(login_url + '?' + urllib.urlencode(login_params)))
        resp.set_cookie('state', login_params['state'])
        return resp
        
    if 'state' in request.args and request.cookies['state'] == request.args['state']:
        if 'error' in request.args:
            return str(request.args)
        else:
            # get an access token
            access_params = {}
            access_params['client_id'] = FACEBOOK_APP_ID
            access_params['redirect_uri'] = request.base_url
            access_params['client_secret'] = FACEBOOK_APP_SECRET
            access_params['code'] = request.args['code']

            response = urlfetch.fetch(access_url + '?' + urllib.urlencode(access_params))

            response_data = urlparse.parse_qs(response.content)

            # get an extended access token
            extension_params = {}
            extension_params['grant_type'] = 'fb_exchange_token'
            extension_params['client_id'] = FACEBOOK_APP_ID
            extension_params['client_secret'] = FACEBOOK_APP_SECRET
            extension_params['fb_exchange_token'] = response_data['access_token'][0]

            response = urlfetch.fetch(access_url + '?' + urllib.urlencode(extension_params))

            response_data = urlparse.parse_qs(response.content)

            access_token = response_data['access_token'][0]
            expires = int(response_data['expires'][0])
            expiration_date = dt.datetime.now() + dt.timedelta(0,expires)


            response = urlfetch.fetch('https://graph.facebook.com/me?access_token='+access_token)

            response_data = json.loads(response.content)

            username = response_data['username']

            # delete all existing tokens for this user
            query = models.AccessTokenModel.all()
            query.filter('username =', username)

            tokens = query.fetch(query.count())
            for token in tokens:
                token.delete()
            
            token = models.AccessTokenModel(username=username,
                                            access_token=access_token,
                                            expiration=expiration_date)

            token.put()

            return redirect(url_for('fb_admin_main'))
                                                   
    else:
        return str(request.arg)