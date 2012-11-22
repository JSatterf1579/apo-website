"""
This module contains the models used in the service package

.. module:: application.service.models

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

from google.appengine.ext import db
from google.appengine.ext.db.polymodel import PolyModel

from application.accounts.models import UserModel
from application.models import EventModel

# Taken from the Service Event tracking section of the design document
class ServiceEventModel(EventModel):
    """This models a service event
    
    .. method:: ServiceEvent([maxBro[,addInfo]])

       Creates a new ServiceEvent entity

       :param maxBro: Maximum number of brothers allowed at service Event
       :type maxBro: int
    
       :param addInfo: Additional information about service event
       :type addInfo: unicode
    
       :rtype: ServiceEvent
    """
    maxBro = db.IntegerProperty()
    addInfo = db.StringProperty()

class ServiceSignUpModel(db.Model):
    """This maps Users to ServiceEvents

    .. method:: ServiceSignUp(user, event)

       Creates a new ServiceSignUp entity

       :param user: User for service event sign up
       :type user: application.models.User
    
       :param event: Event that user is signing up for
       :type event: application.models.Event
    """
    user = db.ReferenceProperty(UserModel, required=True)
    event = db.ReferenceProperty(ServiceEventModel, required=True)

class ServiceReportModel(PolyModel):
    """This is the abstract base type of ServiceReport

    .. method:: ServiceReport()

       Creates a new ServiceReport entity

    .. warning::
       This class is an abstract base class. Do not to be instantiate an instance of this class
    """
    pass

class InsideServiceReportModel(ServiceReportModel):
    """This is the Service Report type for an inside service event

    .. method:: InsideServiceReport(event)

       Creates a new InsideServiceReport entity

       :param event: Service Event that this report is for
       :type event: application.models.ServiceEvent
    """
    event = db.ReferenceProperty(ServiceEventModel, required=True)

class OutsideServiceReportModel(ServiceReportModel):
    """This is the Service Report type for an outside service event

    .. method:: OutsideServiceReport(name, desc, loc, date)

       Creates a new OutsideServiceReport entity

       :param name: Name of event this report is for
       :type name: unicode

       :param desc: Description of event this report is for
       :type desc: unicode

       :param loc: Description of location of event this report is for
       :type loc: unicode

       :param date: Date of event this report is for
       :type date: datetime.date
    """
    name = db.StringProperty(required=True)
    desc = db.StringProperty(required=True)
    loc = db.StringProperty(required=True) # consider changing this to Location reference
    date = db.DateTimeProperty(required=True)

class ServiceHourModel(db.Model):
    """Maps the hours for each brother to a Service Report

    .. method:: ServiceHour(user, report, minutes[, dMinutes])

       Creates a new ServiceHour entity

       :param user: User this service hour is for
       :type user: application.models.User

       :param report: Service report this hour entry is for
       :type report: application.models.ServiceReport

       :param minutes: Number of minutes of service provided
       :type minutes: int

       :param dMinutes: Number of minutes spent driving
       :type dMinutes: int
    """
    # Required Attributes
    user = db.ReferenceProperty(UserModel, required=True)
    report = db.ReferenceProperty(ServiceReportModel, required=True)

    # Optional Attributes
    hours = db.IntegerProperty()
    minutes = db.IntegerProperty(default=0)

# Taken from the Member Contract section of the design document
class ChapterEventModel(EventModel):
    """Takes care of a chapter meeting

    .. method:: ChapterEvent()

       Creates a new ChapterEvent entity
    """
    pass
