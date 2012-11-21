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
    