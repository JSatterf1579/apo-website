"""
This module contains the models for the setup
package

.. module:: application.setup.models

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

from google.appengine.ext import db

class SetupModel(db.Model):
        """
        This model will be used to
        store which versions have
        been configured
        """

        version = db.StringProperty(required=True)