"""
This module contains the models used in the blog.

.. module:: application.blog.models

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

from google.appengine.ext import db
from application.accounts.models import UserModel

class PostModel(db.Model):
    """
    Contains a Post for the blog

    .. method:: PostModel(title, timestamp, text, author)

       Creates a new PostModel Entity

       :param title: The title of this post
       :type title: unicode

       :param timestamp: The time this post was created
       :type timestamp: datetime.datetime

       :param text: The html text of this post
       :type text: unicode

       :param author: The user that created this Post
       :type author: application.accounts.models.UserModel
    """

    title = db.StringProperty(required=True)
    timestamp = db.DateTimeProperty(required=True)
    text = db.StringProperty(required=True, multiline=True)
    author = db.ReferenceProperty(UserModel, required=True)

class CommentModel(db.Model):
    """
    Contains a Comment for a Post

    .. method:: CommentModel(post, timestamp, text, author)

    """

    post = db.ReferenceProperty(PostModel, required=True)
    timestamp = db.DateTimeProperty(required=True)
    text = db.StringProperty(required=True)
    author = db.ReferenceProperty(UserModel, required=True)

