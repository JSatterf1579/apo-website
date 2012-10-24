"""This module contains all of the app engine models for the application

.. module:: models

.. moduleauthor:: Devin Schwab <dts34@case.edu>
.. moduleauthor:: Jon Chan <jtc77@case.edu>
"""


from google.appengine.ext import db
from google.appengine.ext.db import polymodel

# Taken from the member profile section of the design document
class Family(db.Model):
    """Contains the various families

    .. method:: Family(name)

       Creates a new Family entity

       :param name: Name of the Family - e.g. Boehms
       :type name: unicode
    """
    name = db.StringProperty(required=True)

class Contract(db.Model):
    """Stores contract types

    .. method:: Contract(name)

       Creates a new Contract entity

       :param name: Name of contract - e.g. associate
       :type name: unicode
    """
    name = db.StringProperty(required=True)

class User(db.Model):
    """
    Stores user information
    
    .. method:: User(firstName, lastName, cwruID, salt, hash[, middleName, contractType, family, big, avatar])

       Creates a new User entity

       :param firstName: User's first name
       :type firstName: unicode

       :param lastName: User's last name
       :type lastName: unicode

       :param cwruID: User's Case network ID.
       :type cwruID: unicode

       :param salt: A unique string (per user) used in password hashing
       :type salt: unicode

       :param hash: A hash of the user's password with the user's salt
       :type hash: unicode

       :param middleName: User's middle name
       :type middleName: unicode

       :param contractType: User's Contract type
       :type contractType: application.models.Contract

       :param family: User's family
       :type family: application.models.Family

       :param big: User's big
       :type big: application.models.User

       :param avatar: User's gravatar user name
       :type avatar: unicode
    """
    # Required attributes
    firstName = db.StringProperty(required=True)
    lastName = db.StringProperty(required=True)
    cwruID = db.StringProperty(required=True)
    salt = db.StringProperty(required=True)
    hash = db.StringProperty(required=True)

    # Optional attributes
    middleName = db.StringProperty(required=True)
    contractType = db.ReferenceProperty(Contract)
    family = db.ReferenceProperty(Family)
    big = db.SelfReferenceProperty()
    avatar = db.StringProperty()

class Role(db.Model):
    """Contains the various roles in the chapter. Used in permissions

    .. method:: Role(name[, desc])

       Creates a new Role entity

       :param name: Name of the Role - e.g. admin
       :type name: unicode

       :param desc: Description of the Role
       :type desc: unicode
    """
    name = db.StringProperty(required=True)
    desc = db.StringProperty()

class UserRole(db.Model):
    """Maps a User to a Role

    .. method:: UserRole(user, role)

       Creates a new UserRole entity

       :param user: The User associated with this UserRole entity
       :type user: application.models.User

       :param role: The Role associated with this UserRole entity
       :type role: application.models.Role
    """
    user = db.ReferenceProperty(User,required=True)
    role = db.ReferenceProperty(Role, required=True)

class Address(db.Model):
    """Contains an address for a User

    .. method:: Address(user, address[, name])

       Creates a new Address entity

       :param user: User this address belongs to
       :type user: application.models.User

       :param address: Address
       :type address: google.appengine.ext.db.PostalAddress 

       :param name: Nickname for Address - e.g. home
       :type name: unicode
    """
    # Required attributes
    user = db.ReferenceProperty(User, required=True)
    address = db.PostalAddressProperty(required=True)

    # Optional attributes
    name = db.StringProperty()

class Email(db.Model):
    """Contains an email address for a User

    .. method:: Email(user, email[, name])

       Creates a new Email entity

       :param user: User this email address belongs to
       :type user: application.model.User

       :param email: User's email
       :type email: google.appengine.ext.db.Email

       :param name: Optional nickname for address - e.g. school
       :type name: unicode
    """
    # Required attributes
    user = db.ReferenceProperty(User, required=True)
    email = db.EmailProperty(required=True)

    # Optional attributes
    name = db.StringProperty()

class PhoneNumber(db.Model):
    """Contains a phone number for a User

    .. method:: PhoneNumber(user, number[, name])

       Creates a new PhoneNumber entity

       :param user: User this phone number belongs to
       :type user: application.model.User

       :param number: Phone number with in the following format "(111) 555-3333"
       :type number: google.appengine.ext.db.PhoneNumber

       :param name: Optional nickname for phone number - e.g. cell
       :type name: unicode
    """
    # Required Attributes
    user = db.ReferenceProperty(User, required=True)
    number = db.PhoneNumberProperty(required=True)

    #Optional Attributes
    name = db.StringProperty()

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
    # Required Attributes
    name = db.StringProperty(required=True)
    date = db.DateProperty(required=True)
    startTime = db.TimeProperty(required=True)
    endTime = db.TimeProperty(required=True)

    # Optional Attributes
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
    # Required Attributes
    name = db.StringProperty(required=True)
    event = db.ReferenceProperty(Event, required=True)

    # Optional Attributes
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
    """This is the abstract base type of ServiceReport

    .. method:: ServiceReport()

       Creates a new ServiceReport entity

    .. warning::
       This class is an abstract base class. Do not to be instantiate an instance of this class
    """
    pass

class InsideServiceReport(ServiceReport):
    """This is the Service Report type for an inside service event

    .. method:: InsideServiceReport(event)

       Creates a new InsideServiceReport entity

       :param event: Service Event that this report is for
       :type event: application.models.ServiceEvent
    """
    event = db.ReferenceProperty(ServiceEvent, required=True)

class OutsideServiceReport(ServiceReport):
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

class ServiceHour(db.Model):
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
    user = db.ReferenceProperty(User, required=True)
    report = db.ReferenceProperty(ServiceReport, required=True)
    minutes = db.IntegerProperty(required=True)

    # Optional Attributes
    dMinutes = db.IntegerProperty()

# Taken from the Member Contract section of the design document
class ChapterEvent(Event):
    """Takes care of a chapter meeting

    .. method:: ChapterEvent()

       Creates a new ChapterEvent entity
    """
    pass

class Requirement(polymodel.PolyModel):
    """A general base class for a contract requirement

    .. method:: Requirement(contract, dueDate[, name])

       Creates a new Requirement entity

       :param contract: Contract this requirement is associated with
       :type contract: application.models.Contract

       :param dueDate: Date this requirement is due
       :type dueDate: datetime.date

       :param name: Optional nickname for requirement - e.g. inside hours
       :type name: unicode
    """
    # Required Attributes
    contract = db.ReferenceProperty(Contract, required=True)
    dueDate = db.DateProperty(required=True)

    # Optional Attributes
    name = db.StringProperty()

class HourReq(Requirement):
    """Models Service Hours Requirements

    .. method:: HourReq(min, type)

       Creates a new HourReq entity

       :param min: Minutes needed to meet this requirement
       :type min: int

       :param type: Type of minutes needed - e.g. inside
       :type type: unicode
    """
    min = db.IntegerProperty(required=True)
    type = db.StringProperty(required=True)

class DuesReq(Requirement):
    """Models Dues Requirements

    .. method:: DuesReq(amount)

       Creates a new DuesReq entity

       :param amount: Amount of money need to meet this requirement
       :type amount: float
    """
    amount = db.FloatProperty(required=True)

class AttendanceReq(Requirement):
    """Models Attendance Requirements

    .. method:: AttendanceReq(amount, type)

       Creates a new AttendanceReq entity

       :param amount: Amount of events needed to meet this requirement. Allows for fractions of events to be specified
       :type amount: float

       :param type: Type of event needed - e.g. ServiceEvent
       :type type: unicode
    """
    amount = db.FloatProperty(required=True)
    type = db.StringProperty(required=True)

# Taken from the blog section of the design document
class Post(db.Model):
    """Contains a Blog Post

    .. method:: Post(title, datetime, text, author)

       Creates a new Post entity

       :param title: Title of Blog post
       :type title: unicode

       :param datetime: Date and time of posting
       :type datetime: datetime.datetime

       :param text: Content of post
       :type text: unicode

       :param author: User that made this post
       :type author: application.models.User
    """
    title = db.StringProperty(required=True)
    datetime = db.DateTimeProperty(required=True)
    text = db.StringProperty(required=True)
    author = db.ReferenceProperty(User, required=True)

class Comment(db.Model):
    """Contains a comment for a Blog Post

    .. method:: Comment(post, datetime, author, text)

       Creates a new Comment entity

       :param post: Post this comment is associated with
       :type post: application.models.Post

       :param datetime: Date and time of comment
       :type datetime: datetime.datetime

       :param author: User that posted this comment
       :type author: application.models.User

       :param text: Content of comment
       :type text: unicode
    """
    post = db.ReferenceProperty(Post, required=True)
    datetime = db.DateTimeProperty(required=True)
    author = db.ReferenceProperty(User, required=True)
    text = db.StringProperty(required=True)

