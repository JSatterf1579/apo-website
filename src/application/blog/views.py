"""
This module contains the views for the blog package

.. module:: application.blog.views

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

from flaskext.flask_login import current_user, login_required

from application import app

from application.accounts.accounts import require_roles, find_users

from application.accounts.models import RoleModel, UserRoleModel

import forms
import models

from flask import render_template, flash, url_for, redirect, request, jsonify

import datetime as dt

@app.route('/', methods=['GET', 'POST'])
def display_blog():
    """
    View to display existing blog posts
    """

    query = UserRoleModel.all()
    query.filter('user =', current_user.key())

    uroles = query.fetch(query.count())

    new_post = None
    for urole in uroles:
        if urole.role.name == 'webmaster':
            new_post = forms.NewPostForm()
            break


    query = models.PostModel.all()
    query.order('-timestamp')

    posts = query.fetch(10)

    post_form = forms.NewPostForm()

    if request.method == 'POST' and post_form.validate():
        post = models.PostModel(title=post_form.title.data,
                                timestamp=dt.datetime.now(),
                                text=post_form.text.data,
                                author=current_user.key())
        post.put()
        
        posts.insert(0, post)
        if len(posts) > 10:
            del posts[-1]

        
    return render_template('blogs/display_posts.html',
                           new_post=new_post,
                           posts=posts)

