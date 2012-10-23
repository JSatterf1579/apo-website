"""
.. module:: models
   :synopsis: This module contains all of the app engine models for the application

.. moduleauthor:: Devin Schwab <dts34@case.edu>
.. moduleauthor:: Jon Chan <jtc77@case.edu>
"""


from google.appengine.ext import db
from google.appengine.ext.db import polymodel

# Taken from the member profile section of the design document
class User(db.Model):
    """Models a user account"""
    pass

class UserRole(db.Model):
    """Maps a User to a Role"""
    pass

class Role(db.Model):
    """Contains the various roles in the chapter. Used in permissions"""
    pass

class Family(db.Model):
    """Contains the various families"""
    pass

class Address(db.Model):
    """Contains an address for a User"""
    pass

class Email(db.Model):
    """Contains an email address for a User"""
    pass

class PhoneNumber(db.Model):
    """Contains a phone number for a User"""
    pass

class ExampleModel(db.Model):
    """Example Model"""
    example_name = db.StringProperty(required=True)
    example_description = db.TextProperty(required=True)
    added_by = db.UserProperty()
    timestamp = db.DateTimeProperty(auto_now_add=True)

class Event(polymodel.PolyModel):
    """This models a general event type."""
    name = db.StringProperty(required=True)
    date = db.DateProperty(required=True)
    startTime = db.TimeProperty(required=True)
    endTime = db.TimeProperty(required=True)
    description = db.StringProperty()

class Location(db.Model):
    """This models a general location. For use with an event."""
    name = db.StringProperty(required=True)
    event = db.ReferenceProperty(Event, required=True)
    address = db.PostalAddressProperty()

# Taken from the Service Event tracking section of the design document
class ServiceEvent(Event):
    """This models a service event"""
    maxBro = db.IntegerProperty()
    addInfo = db.StringProperty()

class ServiceSignUp(db.Model):
    """This maps Users to ServiceEvents"""
    user = db.ReferenceProperty(User, required=True)
    event = db.ReferenceProperty(ServiceEvent, required=True)

class ServiceReport(polymodel.PolyModel):
    """This is the abstract base type of ServiceReport"""
    pass

class InsideServiceReport(ServiceReport):
    """This is the Service Report type for an inside service event"""
    pass

class OutsideServiceReport(ServiceReport):
    """This is the Service Report type for an outside service event"""
    pass

class ServiceHour(db.Model):
    """Maps the hours for each brother to a Service Report"""
    pass

# Taken from the Member Contract section of the design document
class ChapterEvent(Event):
    """Takes care of a chapter meeting"""
    pass

class Contract(db.Model):
    """Stores contract types"""
    pass

class Requirement(polymodel.PolyModel):
    """A general base class for a contract requirement"""
    pass

class HourReq(Requirement):
    """Models Service Hours Requirements"""
    pass

class DuesReq(Requirement):
    """Models Dues Requirements"""
    pass

class AttendanceReq(Requirement):
    """Models Attendance Requirements"""
    pass

# Taken from the blog section of the design document
class Post(db.Model):
    """Contains a Blog Post"""
    pass

class Comment(db.Model):
    """Contains a comment for a Blog Post"""
    pass

