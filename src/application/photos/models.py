"""
This module implements the models used by the photos package
"""

from google.appengine.ext import db

class AlbumModel(db.Model):
    me = db.StringProperty(required=True)

class PhotoModel(db.Model):
    me = db.StringProperty(required=True)
    album = db.ReferenceProperty(AlbumModel, required=True)
    approved = db.BooleanProperty(required=True, default=False)