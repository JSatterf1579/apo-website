"""
This module contains forms used in the blog package

.. module:: application.blogs.forms

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

from flaskext import wtf
from flaskext.wtf import validators

class NewPostForm(wtf.Form):
    """
    Create a new blog post
    """

    title = wtf.TextField('Title*', [validators.Required()])
    text = wtf.TextAreaField('Text*', [validators.Required()])

class NewComment(wtf.Form):
    """
    Create a new comment
    """
    text = wtf.TextAreaField('New Comment', [validators.Required()])

class DeletePostForm(wtf.Form):
    """
    Stores the key associated with a blog post
    so that it can be deleted
    """

    key = wtf.HiddenField('key', [validators.Required()])

class DeleteCommentForm(wtf.Form):
    """
    Stores the key associated with a comment
    so that it can be deleted
    """
    key = wtf.HiddenField('key', [validators.Required()])