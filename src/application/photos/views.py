"""
This module contains the views needed for the photo gallery features
of the website
"""

from flaskext.flask_login import current_user, login_required

from application import app

from flask import render_template, flash, url_for, redirect, request, make_response, jsonify

from flaskext import wtf

import json, urlparse, urllib

import datetime as dt

import models
import forms

from application.facebook import facebook as fb
from application.facebook import models as fb_models

from application.accounts.accounts import require_roles

from google.appengine.api import urlfetch

@app.route('/photos/albums/list')
def photos_album_list():
    """
    View for displaying a list of all albums
    """

    query = fb_models.UserAccessTokenModel.all()
    query.filter('use_albums =', True)

    user_tokens = query.fetch(query.count())

    query = fb_models.PageAccessTokenModel.all()
    query.filter('use_albums =', True)

    page_tokens = query.fetch(query.count())

    albums = []
    for token in user_tokens:
        album_list = fb.AlbumList(token)
        album_dict = album_list.get_all_albums_by_name()
        for key in album_dict:
            albums.append(album_dict[key])
        
    for token in page_tokens:
        album_list = fb.AlbumList(token)
        album_dict = album_list.get_all_albums_by_name()
        for key in album_dict:
            albums.append(album_dict[key])

    return render_template('photos/list_albums.html',
                           albums=albums)

