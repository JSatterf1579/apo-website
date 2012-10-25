"""
forms.py

Web forms based on Flask-WTForms

See: http://flask.pocoo.org/docs/patterns/wtforms/
     http://wtforms.simplecodes.com/

"""

from flaskext import wtf
from flaskext.wtf import validators


class ExampleForm(wtf.Form):
    example_name = wtf.TextField('Name', validators=[validators.Required()])
    example_description = wtf.TextAreaField('Description', validators=[validators.Required()])

class LogInForm(Form):
    """This is the Log In form
    
    .. method:: LogInForm(username, password)
    
       :param username: Username of user
       :type username: unicode
       :param password: Password of user
       :type password: unicode
       
       :rtype: Form instance
    """   
    username = TextField('Username: ',[validators.Required()])
    password = PasswordField('Password: ',[validators.Required()])
	
class CreateServiceEventForm(Form):
    """This is the Create a Service Event Form
    
    .. method:: CreateServiceEventForm(name, date, startTime, endTime, location[, summary, maxBrothers])
    
       :param name: Name of event
       :type name: unicode
       :param date: Date of the event 
       :type date: datetime.date
       :param startTime: Time event starts at
       :type startTime: datetime.time
       :param endTime: Time event ends at        
       :type endTime: datetime.time
       :param location: Location of the event
       :type location: application.models.Location
       :param summary: Description of the event
       :type summary: unicode
       :param maxBrothers: Maximum Number of Brothers
       :type maxBrothers: int
        
       :rtype: Form instance
    """
    name = TextField('Name: ',validators=[validators.Required()])
    date = wtf.TextField('Date: ', validators=[validators.Required()])
    startTime = wtf.TextField('Start Time: ', validators=[validators.Required()])
    endTime = TextField('End Time: ', validators=[validators.Required()])
    location = wtf.TextAreaField('Location: ', validators=[validators.Required()])
    summary = wtf.TextAreaField('Summary: ', validators=[validators.Required()])
    maxBrothers = wtf.Textfield('Max # of brothers: ', validators=[validators.Optional()])
    
class EventSignUpForm(Form):
    """Event Sign up form
    .. method:: EventSignUpForm(name)
        
       :param name: Name of brother
       :type name: unicode
           
       :rtype: Form instance
    """
    name = TextField('Name: ', validators=[validators.Required()])

class CreateUpdateContractForm(Form):
    """Form for Creating and Updating Contract types
    .. method:: CreateUpdateContractForm(name, hours, minutes, hoursDueDate, amount, duesDueDate, attendanceReq, attDueDate)
        
       :param name: Name of contract
       :type name: unicode       
       :param hours: Hours needed to fulfill contract
       :type hours: int
       :param minutes: Minutes needed to fulfill contract
       :type minutes: int
       :param hoursDueDate: Date that all hours and minutes must be completed
       :type hoursDueDate: datetime.date
       :param amount: Dues owed
       :type amount: int
       :param duesDueDate: Date that dues must be paid by
       :type duesDueDate: datetime.date
       :param attendanceReq: Number of chapter meetings that must be attended
       :type attendanceReq: int
       :param attDueDate: Date that the required number of attended meetings must be met by
       :type attDueDate: datetime.date
       
       :rtype: Form instance
    """
    name = TextField('Name: ',validators=[validators.Required()])
    hours = TextField('Hours: ',validators=[validators.Required()])
    min = TextField('Minutes: ',validators=[validators.Required()])
    hoursDueDate = TextField('Hours Due Date: ',validators=[validators.Required()])
    amount = TextField('Dues Amount: 'validators=[validators.Required()])
    duesDueDate = TextField('Dues Due Date: ',validators=[validators.Required()])
    attendanceReq = TextField('Attendance Requirements: ',validators=[validators.Required()])
    attDueDate = TextField('Attendance Due Date: ',validators=[validators.Required()])

class CreateUpdateProfileForm(Form):
    """Form for Creating and Updating User Profiles
    .. method:: CreateUpdateProfileForm(fname, mname, lname, caseid, avatar, contract[, family, big])
       
       :param fname: Brother's first name
       :type fname: unicode
       :param mname: Brother's middle name
       :type mname: unicode
       :param lname: Brother's last name
       :type lname: unicode
       :param caseid: Brother's Case ID
       :type caseid: unicode
       :param avatar: Brother's avatar URL
       :type avatar: unicode
       :param contract: Brother's signed contract type
       :type contract: application.model.Contract
       :param family: Brother's assigned family
       :type family: application.model.Family
       :param big: Brother's assigned big
       :type big: unicode
       
       :rtype: Form instance
    """
    fname = TextField('First Name: ',validators=[validators.Required()])
    mname = TextField('Middle Name: ',validators=[validators.Optional()])
    lname = TextField('Last Name: ',validators=[validators.Required()])
    caseid = TextField('Case ID: ',validators=[validators.Required()])
    contract = TextField('Contract type: ',validators=[validators.Required()])
    family = TextField('Family: ',validators=[validators.Optional()])
    big = TextField('Big: ',validators=[validators.Optional()])
    avatar = TextField('Avatar: ',validators=[validators.Required()])
    
class CreateBlogForm(Form):
    """Form for creating a blog post
    .. method:: CreateBlogForm(title, blog)
    
       :param title: Title of the blog post
       :type title: unicode
       :pararm blog: Content of the blog post
       :type blog: unicode
       
       :rtype: Form instance
    """
    title = TextField('Title: ',validators=[validators.Required()])
    blog = TextAreaField('Blog entry: ',validators=[validators.Required()])

class CreateCommentForm(Form):
    """Form for making a comment on a blog post
    .. method:: CreateCommentForm(comment)
       
       :param comment: Comment to be posted on the blog
       :type comment: unicode
       
       :rtype: Form instance
    """
    comment = TextAreaField('Comment: ',validators=[validators.Required()])
    
class OrganizePhotoForm(Form):
    """Form for adding a photo to a photo album
    .. method:: OrganizePhotoForm(albumName, photo)
       
       :param albumName: Name of photo album
       :type albumName: unicode
       :param photo: Photo URL
       :type photo: unicode
       
       :rtype: Form instance
    """
    albumName = TextField('Album Name: ',validators=[validators.Required()])
    photo = TextField('Photo URL: ',validators=[validators.Required()])
    
class SubmitPhotoForm(Form);
    """Form for submitting a photo to the website
    .. method:: SubmitPhotoForm(name, photo)
       
       :param name: Brief description of photo
       :type albumName: unicode
       :param photo: Photo URL
       :type photo: unicode
       
       :rtype: Form instance
    """
    name = TextField('Photo Name: ',validators=[validators.Required()])
    photo = TextField('Photo URL: ',validators=[validators.Required()])
    
    