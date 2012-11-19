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
import pdb

from flaskext.flask_login import current_user, login_required

from application import app

from flask import render_template, flash, url_for, redirect, request, make_response, jsonify

import json, urlparse, urllib

import datetime as dt

import models

from application.accounts.accounts import require_roles

from google.appengine.api import urlfetch
from google.appengine.ext import db

from secret_keys import FACEBOOK_APP_ID, FACEBOOK_APP_SECRET
from application.generate_keys import generate_randomkey

@app.route('/facebook/admin')
@require_roles(names=['webmaster'])
def fb_admin_main():
    """
    UI for managing facebook related settings
    """
    
    query = models.UserAccessTokenModel.all()

    user_tokens = query.fetch(query.count())

    for token in user_tokens:
        token.time_left = str(token.expiration - dt.datetime.now())

    query = models.PageAccessTokenModel.all()

    page_tokens = query.fetch(query.count())

    query = models.AppAccessTokenModel.all()

    app_tokens = query.fetch(query.count())
        
    return render_template('facebook/admin.html',
                           user_tokens=user_tokens,
                           page_tokens=page_tokens,
                           app_tokens=app_tokens)

@app.route('/facebook/admin/delete-user-access/<username>')
@require_roles(names=['webmaster'])
def fb_admin_del_user_access(username):
    """
    Removes all tokens for a given user from the datastore
    """
    query = models.UserAccessTokenModel.all()
    query.filter('username =', username)

    tokens = query.fetch(query.count())

    # find all tokens associated with that user
    assoc_tokens = []
    for token in tokens:
        query = models.PageAccessTokenModel.all()
        query.filter('user_token =', token.key())

        assoc_tokens += query.fetch(query.count())

        query = models.AppAccessTokenModel.all()
        query.filter('user_token =', token.key())

        assoc_tokens += query.fetch(query.count())

    # delete user token and all assoicated tokens
    db.delete(assoc_tokens)
    db.delete(tokens)

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
        login_params['scope'] = 'manage_pages,user_groups'

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
            try:
                expires = int(response_data['expires'][0])
            except KeyError:
                expires = 60*24*60*60
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
            
            token = models.UserAccessTokenModel(username=username,
                                            access_token=access_token,
                                            expiration=expiration_date)

            token.put()

            return redirect(url_for('fb_admin_get_assoc_tokens'))
                                                   
    else:
        return str(request.arg)

@app.route('/facebook/admin/get-assoc-tokens')
@require_roles(names=['webmaster'])
def fb_admin_get_assoc_tokens():
    """
    Returns the list of pages associated with each of the tokens
    in the datastore
    """

    base_url = 'https://graph.facebook.com/me/accounts'
    
    query = models.UserAccessTokenModel.all()

    tokens = query.fetch(query.count())


    for token in tokens:
        params = {'access_token': token.access_token}

        response = urlfetch.fetch(base_url + '?' + urllib.urlencode(params))

        response_data = json.loads(response.content)

        for token_data in response_data['data']:

            if token_data['category'].lower() == 'application':
                app_token = models.AppAccessTokenModel(name=token_data['name'],
                                                       user_token=token.key(),
                                                       app_id=token_data['id'],
                                                       category=token_data['category'],
                                                       access_token=token_data['access_token'],
                                                       expiration=token.expiration)
                app_token.put()
            else:
                page_token = models.PageAccessTokenModel(name=token_data['name'],
                                                         user_token=token.key(),
                                                         page_id=token_data['id'],
                                                         perms=token_data['perms'],
                                                         category=token_data['category'],
                                                         access_token=token_data['access_token'],
                                                         expiration=token.expiration)
                page_token.put()

        flash('Successfully retrieved access %s along with associated pages and apps permissions' %
              token.username, 'success')
    return redirect(url_for('fb_admin_main'))
