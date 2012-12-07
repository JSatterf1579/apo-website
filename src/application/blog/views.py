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

import urllib, urlparse

@app.route('/blog', methods=['GET', 'POST'])
def display_blog():
    """
    View to display existing blog posts
    """
    new_post = None
    if current_user.is_authenticated():
        query = UserRoleModel.all()
        query.filter('user =', current_user.key())

        uroles = query.fetch(query.count())

        for urole in uroles:
            if urole.role.name == 'webmaster':
                new_post = forms.NewPostForm()
                break


    query = models.PostModel.all()
    query.order('-timestamp')

    posts = query.fetch(10)

    for post in posts:
        post.url_timestamp = urllib.quote_plus(str(post.timestamp))
        post.url_title = urllib.quote_plus(post.title)

    post_form = forms.NewPostForm()

    if request.method == 'POST' and post_form.validate():
        post = models.PostModel(title=post_form.title.data,
                                timestamp=dt.datetime.now(),
                                text=post_form.text.data,
                                author=current_user.key())
        post.put()

        post.url_timestamp = urllib.quote_plus(str(post.timestamp))
        post.url_title = urllib.quote_plus(post.title)
        
        posts.insert(0, post)
        if len(posts) > 10:
            del posts[-1]

        post_form = forms.NewPostForm(None)

    post_form = forms.NewPostForm(None)
        
        
    return render_template('blogs/display_posts.html',
                           new_post=new_post,
                           posts=posts)

@app.route('/blog/view/<timestamp>/<title>', methods=['GET', 'POST'])
def view_blog_post(timestamp, title):
    """
    View to display blog post and associated comments
    """

    edit_post = None
    # determine if the user has the proper role to edit
    if current_user.is_authenticated():
        query = UserRoleModel.all()
        query.filter('user =', current_user.key())

        uroles = query.fetch(query.count())


        for urole in uroles:
            if urole.role.name == 'webmaster':
                edit_post = True
                break

    # get the blog posts
    query = models.PostModel.all()
    str_timestamp = urllib.unquote_plus(timestamp)
    timestamp = dt.datetime.strptime(str_timestamp, '%Y-%m-%d %H:%M:%S.%f')
    query.filter('timestamp =', timestamp)
    query.filter('title =', urllib.unquote_plus(title))
    
    try:
        post = query.fetch(1)[0]
    except IndexError:
        return render_template('404.html'), 404

    # add the urlencoded version of timestamp and 
    post.url_timestamp = urllib.quote_plus(str(post.timestamp))
    post.url_title = urllib.quote_plus(post.title)
        
    # get the comments
    query = models.CommentModel.all()
    query.filter('post =', post.key())
    query.order('timestamp')

    comments = query.fetch(query.count())

    # go through and add forms with delete button to each comment if the user
    # has edit privileges
    if edit_post is not None:
        for comment in comments:
            comment.delete = forms.DeleteCommentForm(None)
            comment.delete.key.data = comment.key()
            comment.url_timestamp = urllib.quote_plus(str(comment.timestamp))

    form = forms.NewComment(request.form)
    if request.method=="POST" and form.validate():
        comment = models.CommentModel(post=post.key(),
                                      timestamp=dt.datetime.now(),
                                      text=form.text.data,
                                      author=current_user.key())
        comment.put()
        comment.delete = forms.DeleteCommentForm(None)
        comment.delete.key.data = comment.key()
        comment.url_timestamp = urllib.quote_plus(str(comment.timestamp))

        comments.append(comment)
        
    return render_template('blogs/display_post.html',
                           edit_post=edit_post,
                           current_user=current_user,
                           post=post,
                           comments=comments,
                           new_comment=forms.NewComment(None))

@app.route('/blog/delete/<timestamp>/<title>')
@require_roles(names=['webmaster'])
def delete_blog_post(timestamp, title):
    """
    View to delete the blog post specified
    by the timestamp and title
    """

    # get the blog posts
    query = models.PostModel.all()
    str_timestamp = urllib.unquote_plus(timestamp)
    timestamp = dt.datetime.strptime(str_timestamp, '%Y-%m-%d %H:%M:%S.%f')
    query.filter('timestamp =', timestamp)
    query.filter('title =', urllib.unquote_plus(title))
    
    try:
        post = query.fetch(1)[0]
    except IndexError:
        return render_template('404.html'), 404

    query = models.CommentModel.all()
    query.filter('post =', post.key())

    comments = query.fetch(query.count())

    for comment in comments:
        comment.delete()

    post.delete()

    return redirect(url_for('display_blog'))
    
@app.route('/blog/edit/<timestamp>/<title>', methods=['GET', 'POST'])
@require_roles(names=['webmaster'])
def edit_blog_post(timestamp, title):
    """
    View to edit an exsiting blog specified
    by the timestamp and title
    """
    # get the blog posts
    query = models.PostModel.all()
    str_timestamp = urllib.unquote_plus(timestamp)
    timestamp = dt.datetime.strptime(str_timestamp, '%Y-%m-%d %H:%M:%S.%f')
    query.filter('timestamp =', timestamp)
    query.filter('title =', urllib.unquote_plus(title))
    
    try:
        post = query.fetch(1)[0]
    except IndexError:
        return render_template('404.html'), 404

    post.url_timestamp = urllib.quote_plus(str(post.timestamp))
    post.url_title = urllib.quote_plus(post.title)
        
    post_form = forms.NewPostForm()
    if request.method == "POST" and post_form.validate():
        query = models.CommentModel.all()
        query.filter('post =', post.key())

        comments = query.fetch(query.count())
        
        new_post = models.PostModel(title=post_form.title.data,
                                    timestamp=dt.datetime.now(),
                                    text=post_form.text.data,
                                    author=current_user.key())

        new_post.put()

        for comment in comments:
            comment.post = new_post.key()
            comment.put()

        post.delete()

        new_post.url_timestamp = urllib.quote_plus(str(new_post.timestamp))
        new_post.url_title = urllib.quote_plus(new_post.title)

        return redirect(url_for('view_blog_post',
                                timestamp=new_post.url_timestamp,
                                title=new_post.url_title))
        
    edit_post_form = forms.NewPostForm(None)
    edit_post_form.title.data = post.title
    edit_post_form.text.data = post.text

    url_timestamp = urllib.quote_plus(str(post.timestamp))
    url_title = urllib.quote_plus(post.title)
    
    return render_template('blogs/edit_post.html',
                           form=edit_post_form,
                           url_timestamp=url_timestamp,
                           url_title=url_title)
        
@app.route('/blog/delete/comment/<author>/<timestamp>')
def delete_blog_comment(author, timestamp):
    """
    View to delete a single comment
    specified by author and timestamp
    """

    author = find_users(1,cwruid=('=', author))[0]

    query = models.CommentModel.all()
    query.filter('author =', author.key())
    str_timestamp = urllib.unquote_plus(timestamp)
    timestamp = dt.datetime.strptime(str_timestamp, '%Y-%m-%d %H:%M:%S.%f')
    query.filter('timestamp =', timestamp)

    comment = query.fetch(1)[0]

    url_timestamp = urllib.quote_plus(str(comment.post.timestamp))
    url_title = urllib.quote_plus(comment.post.title)

    comment.delete()

    return redirect(url_for('view_blog_post',
                            timestamp=url_timestamp,
                            title=url_title))