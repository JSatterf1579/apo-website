"""
This module implements the forms that are used by the photos package
"""

from flaskext import wtf
from flaskext.wtf import validators

class DisplayOptForm(wtf.Form):
    disp_opt = wtf.BooleanField('Display', [validators.Optional()])
    obj_id = wtf.HiddenField('ID', [validators.Optional()])

class MultiDisplayOptForm(wtf.Form):
    disp_opts = wtf.FieldList(wtf.FormField(DisplayOptForm))

class EditAlbumForm(wtf.Form):
    album_name = wtf.TextField('Album Name', [validators.Required()])
    album_desc = wtf.TextField('Album Description', [validators.Optional()])
    disp_opts = wtf.FieldList(wtf.FormField(DisplayOptForm))