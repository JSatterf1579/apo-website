"""
This module contains the datastore models
needed for the facebook package.

.. module:: application.facebook.models

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

from google.appengine.ext import db

class AccessTokenModel(db.Model):
    username = db.StringProperty(required=True)
    access_token = db.StringProperty(required=True)
    expiration = db.DateTimeProperty(required=True)