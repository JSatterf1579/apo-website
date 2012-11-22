"""This module contains all of the app engine models for the application

.. module:: models

.. moduleauthor:: Devin Schwab <dts34@case.edu>
.. moduleauthor:: Jon Chan <jtc77@case.edu>
"""


from google.appengine.ext import db
from google.appengine.ext.db import polymodel

import flaskext.flask_login as login

class EventModel(polymodel.PolyModel):
    """This models a general event type

    .. method:: Event(name, date, startTime, endTime[, description])

       Creates a new Event entity

       :param name: Name of event
       :type name: unicode
    
       :param date: Date of the event
       :type date: datetime.date
    
       :param startTime: Time event starts at
       :type startTime: datetime.time
    
       :param endTime: Time event ends at
       :type endTime: datetime.time
    
       :param description: Description of the event
       :type description: unicode

       :rtype: Event model instance
    """
    # Required Attributes
    name = db.StringProperty(required=True)
    start_time = db.DateTimeProperty(required=True)
    end_time = db.DateTimeProperty(required=True)
    location = db.PostalAddressProperty(required=True)

    # Optional Attributes
    description = db.StringProperty()


