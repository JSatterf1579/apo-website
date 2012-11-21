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

from flaskext import wtf

import json, urlparse, urllib

import datetime as dt

import models
import forms
import facebook

from application.accounts.accounts import require_roles

from google.appengine.api import urlfetch
from google.appengine.ext import db

from secret_keys import FACEBOOK_APP_ID, FACEBOOK_APP_SECRET
from application.generate_keys import generate_randomkey

from application.decorators import nocache

@app.route('/facebook/admin')
@require_roles(names=['webmaster'])
@nocache
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

    opt_form = forms.MultiAccessTokenOptionsForm(None)

    for i in range(len(user_tokens)):
        opt_form.user_options.append_entry(wtf.FormField(forms.AccessTokenOptionsForm(None)))
        opt_form.user_options[i].use_albums.data = user_tokens[i].use_albums
        opt_form.user_options[i].token_key.data = user_tokens[i].key()

    for i in range(len(page_tokens)):
        opt_form.page_options.append_entry(wtf.FormField(forms.AccessTokenOptionsForm(None)))
        opt_form.page_options[i].use_albums.data = page_tokens[i].use_albums
        opt_form.page_options[i].token_key.data = page_tokens[i].key()
    
    return render_template('facebook/admin.html',
                           token_options=opt_form,
                           user_tokens=user_tokens,
                           page_tokens=page_tokens,
                           app_tokens=app_tokens)

@app.route('/facebook/admin/handle-options/json', methods=['POST'])
@require_roles(names=['webmaster'])
def fb_admin_handle_options():
    """
    Handles the token options form
    """

    opt_form = forms.MultiAccessTokenOptionsForm(request.form)

    query = models.UserAccessTokenModel.all()

    results = query.fetch(query.count())

    user_tokens = {}
    for token in results:
        user_tokens[unicode(token.key())] = token

    query = models.PageAccessTokenModel.all()

    results = query.fetch(query.count())

    page_tokens = {}
    for token in results:
        page_tokens[unicode(token.key())] = token
    
    if opt_form.validate():

        for user_option in opt_form.user_options:
            currToken = user_tokens[user_option.token_key.data]
            currToken.use_albums = user_option.use_albums.data
            currToken.put()

        for page_option in opt_form.page_options:
            currToken = page_tokens[page_option.token_key.data]
            currToken.use_albums = page_option.use_albums.data
            currToken.put()

        return jsonify({'result':'success'})
    else:
        return jsonify({'result':'error'})
    
@app.route('/facebook/admin/delete-user-access/<username>')
@require_roles(names=['webmaster'])
@nocache
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
@nocache
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
        login_params['scope'] = 'manage_pages,user_groups,publish_actions,publish_stream,user_videos,user_photos,photo_upload,read_stream'

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


            fb_admin_del_user_access(username)
            
            token = models.UserAccessTokenModel(username=username,
                                                access_token=access_token,
                                                expiration=expiration_date,
                                                user_id=response_data['id'])

            token.put()

            return redirect(url_for('fb_admin_get_assoc_tokens'))
                                                   
    else:
        return str(request.arg)

@app.route('/facebook/admin/get-assoc-tokens')
@require_roles(names=['webmaster'])
@nocache
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

@app.route('/facebook/test/post/page/text', methods=['GET','POST'])
@require_roles(names=['webmaster'])
@nocache
def fb_admin_post_page_text():
    """
    Tests posting to the pages the website has
    access tokens for
    """

    query = models.PageAccessTokenModel.all()
    page_token = query.fetch(1)[0]

    if request.method == "POST":
        feed_url = 'https://graph.facebook.com/%s/feed' % page_token.page_id

        params = {}
        params['access_token'] = page_token.access_token
        params['message'] = request.form['message']

        response = urlfetch.fetch(feed_url,
                                  method=urlfetch.POST,
                                  payload=urllib.urlencode(params))

        if response.status_code == 200:
            response_data = json.loads(response.content)
            flash('Successfully posted to post id: %s' % response_data['id'],
                  'success')
        else:
            response_data = json.loads(response.content)
            flash('Error %i: %s' % (response_data['error']['code'],
                                    response_data['error']['message']),
                  'error')

    return render_template('facebook/test_post.html',
                           page=page_token,
                           url=request.path)

@app.route('/facebook/test/view/photos', methods=['GET'])
@require_roles(names=['webmaster'])
@nocache
def fb_test_view_photos():
    """
    Tests viewing photos for a user in the database
    """
    import pdb
    tokens = []
    
    query = models.UserAccessTokenModel.all()
    query.filter('use_albums =', True)

    user_tokens = query.fetch(query.count())

    query = models.PageAccessTokenModel.all()
    query.filter('use_albums =', True)

    page_tokens = query.fetch(query.count())

    albums = []
    for token in user_tokens:
        album_list = facebook.AlbumList(token.access_token)
        album_dict = album_list.get_all_albums_by_name()
        for key in album_dict:
            albums.append(album_dict[key])
        
    for token in page_tokens:
        album_list = facebook.AlbumList(token)
        album_dict = album_list.get_all_albums_by_name()
        for key in album_dict:
            albums.append(album_dict[key])

    return render_template('facebook/view_albums.html',
                           albums=albums)


