"""This module contains all of the app engine models for the application

.. module:: models

.. moduleauthor:: Devin Schwab <dts34@case.edu>
.. moduleauthor:: Jon Chan <jtc77@case.edu>
"""


from google.appengine.ext import db
from google.appengine.ext.db import polymodel

# Taken from the member profile section of the design document
class User(db.Model):
    """Stores user information
    
    .. method:: User()

       Creates a new User entity
    """
    pass

class UserRole(db.Model):
    """Maps a User to a Role

    .. method:: UserRole()

       Creates a new UserRole entity
    """
    pass

class Role(db.Model):
    """Contains the various roles in the chapter. Used in permissions

    .. method:: Role()

       Creates a new Role entity
    """
    pass

class Family(db.Model):
    """Contains the various families

    .. method:: Family()

       Creates a new Family entity
    """
    pass

class Address(db.Model):
    """Contains an address for a User

    .. method:: Address()

       Creates a new Address entity
    """
    pass

class Email(db.Model):
    """Contains an email address for a User

    .. method:: Email()

       Creates a new Email entity
    """
    pass

class PhoneNumber(db.Model):
    """Contains a phone number for a User

    .. method:: PhoneNumber()

       Creates a new PhoneNumber entity
    """
    pass

class ExampleModel(db.Model):
    """Example Model"""
    example_name = db.StringProperty(required=True)
    example_description = db.TextProperty(required=True)
    added_by = db.UserProperty()
    timestamp = db.DateTimeProperty(auto_now_add=True)

class Event(polymodel.PolyModel):
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
    name = db.StringProperty(required=True)
    date = db.DateProperty(required=True)
    startTime = db.TimeProperty(required=True)
    endTime = db.TimeProperty(required=True)
    description = db.StringProperty()

class Location(db.Model):
    """This models a general location. For use with an event

    .. method:: Location(name, event[, address])

       Creates a new Location entity

       :param name: Name of Location
       :type name: unicode
       :param event: A reference to an existing Event entity
       :type event: application.models.Event
       :param address: Address of event
       :type address: google.appengine.ext.db.PostalAddress
    """
    name = db.StringProperty(required=True)
    event = db.ReferenceProperty(Event, required=True)
    address = db.PostalAddressProperty()

# Taken from the Service Event tracking section of the design document
class ServiceEvent(Event):
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

class ServiceSignUp(db.Model):
    """This maps Users to ServiceEvents

    .. method:: ServiceSignUp(user, event)

       Creates a new ServiceSignUp entity

       :param user: User for service event sign up
       :type user: application.models.User
       :param event: Event that user is signing up for
       :type event: application.models.Event
    """
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

