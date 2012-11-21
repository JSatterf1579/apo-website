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
from application.accounts.models import UserRoleModel, RoleModel

from google.appengine.api import urlfetch

import facebooksdk as fbsdk

@app.route('/photos/albums/list')
@login_required
def photos_album_list():
    """
    View for displaying a list of all albums
    """

    query = UserRoleModel.all()
    query.filter('user =', current_user.key())

    can_edit = None
    uroles = query.fetch(query.count())
    for urole in uroles:
        if urole.role.name == 'webmaster':
            can_edit=True
            break

    query = fb_models.AlbumModel.all()
    query.filter('display =', True)

    albums = query.fetch(query.count())

    return render_template('photos/list_albums.html',
                           can_edit=can_edit,
                           albums=albums)
    


@app.route('/photos/albums/<album_id>')
@login_required
def photos_show_album(album_id):
    """
    View to display all of an album's
    photos
    """
    query = UserRoleModel.all()
    query.filter('user =', current_user.key())

    can_edit = None
    uroles = query.fetch(query.count())
    for urole in uroles:
        if urole.role.name == 'webmaster':
            can_edit=True
            break

    query = fb_models.PhotoModel.all()
    query.filter('approved =', True)
    query.filter('album_id =', album_id)

    photos = query.fetch(query.count())

    return render_template('photos/show_album.html',
                           can_edit=can_edit,
                           album_id=album_id,
                           photos=photos)
            
@app.route('/photos/albums/edit')
@require_roles(names=['webmaster'])
def photos_edit_albums():
    """
    View to select which albums are displayed
    """
    
    query = fb_models.UserAccessTokenModel.all()
    query.filter('use_albums =', True)

    user_tokens = query.fetch(query.count())

    query = fb_models.PageAccessTokenModel.all()
    query.filter('use_albums =', True)

    page_tokens = query.fetch(query.count())

    form = forms.MultiDisplayOptForm(None)
    
    albums = []
    for token in user_tokens:
        album_list = fb.AlbumList(token)
        album_dict = album_list.get_all_albums_by_name()
        for key in album_dict:
            form.disp_opts.append_entry(wtf.FormField(forms.DisplayOptForm(None)))
            albums.append(album_dict[key].get_model())
            form.disp_opts[-1].disp_opt.data = albums[-1].display
            form.disp_opts[-1].obj_id.data = albums[-1].me
            
    for token in page_tokens:
        album_list = fb.AlbumList(token)
        album_dict = album_list.get_all_albums_by_name()
        for key in album_dict:
            form.disp_opts.append_entry(wtf.FormField(forms.DisplayOptForm(None)))
            albums.append(album_dict[key].get_model())
            form.disp_opts[-1].disp_opt.data = albums[-1].display
            form.disp_opts[-1].obj_id.data = albums[-1].me
            
    return render_template('photos/edit_albums.html',
                           form=form,
                           albums=albums)

@app.route('/photos/albums/edit/json', methods=['POST'])
@require_roles(names=['webmaster'])
def photos_edit_albums_json():
    """
    Handle json POST requests
    """

    form = forms.MultiDisplayOptForm()
    if form.validate():

        query = fb_models.AlbumModel.all()

        results = query.fetch(query.count())

        albums = {}
        for album in results:
            albums[album.me] = album
        
        for opt_form in form.disp_opts:
            album = albums[opt_form.obj_id.data]
            if album.display != opt_form.disp_opt.data:
                album.display = opt_form.disp_opt.data
                album.put()
                
        return jsonify({'result':'success'})
    else:
        return jsonify({'result':'failure', 'errors':form.errors})

@app.route('/photos/albums/edit/<album_id>')
@require_roles(names=['webmaster'])
def photos_edit_album(album_id):
    """
    View to edit the photos in an album
    """

    query = fb_models.AlbumModel.all()
    query.filter('me =', album_id)

    try:
        token = query.fetch(1)[0].token
    except IndexError:
        return render_template('404.html'), 404

    album = fb.Album(token=token, album_id=album_id)

    album_model = album.get_model()
    
    photos = album.get_photos()

    form = forms.EditAlbumForm(None)

    form.album_name.data = album_model.name
    if album_model.desc is not None:
        form.album_desc.data = album_model.desc

    
    for photo in photos:
        form.disp_opts.append_entry(wtf.FormField(forms.DisplayOptForm(None)))
        form.disp_opts[-1].disp_opt.data = photo.approved
        form.disp_opts[-1].obj_id.data = photo.me
        form.photo_names.append_entry(wtf.TextField(None))
        form.photo_names[-1].data = photo.name
    
    return render_template('photos/edit_album.html',
                           album_id=album_id,
                           form=form,
                           photos=photos)

@app.route('/photos/albums/edit/<album_id>/json', methods=['POST'])
@require_roles(names=['webmaster'])
def photos_edit_album_json(album_id):
    """
    View to handle the approval of photos for display
    """
    form = forms.EditAlbumForm()
    if form.validate():

        query = fb_models.AlbumModel.all()
        query.filter('me =', album_id)
        album = None
        try:
            album = query.fetch(1)[0]

            album.name = form.album_name.data
            if form.album_desc.data != '':
                album.desc = form.album_desc.data
            else:
                album.desc = None
            album.put()
        except IndexError:
            return jsonify({'result':'error'}), 404

        query = fb_models.PhotoModel.all()

        results = query.fetch(query.count())

        photos = {}
        for photo in results:
            photos[photo.me] = photo
        
        for i, opt_form in enumerate(form.disp_opts):
            photo = photos[opt_form.obj_id.data]
            if photo.approved != opt_form.disp_opt.data:
                photo.approved = opt_form.disp_opt.data
            photo.name = form.photo_names[i].data
            photo.put()

                
        return jsonify({'result':'success'})
    else:
        return jsonify({'result':'failure', 'errors':form.errors})

    