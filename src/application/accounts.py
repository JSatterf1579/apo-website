"""This module contains methods related to user accounts and logins.

.. module:: accounts

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

from application import login_manager
from application.models import User

from Crypto.Hash import SHA,MD5
from generate_keys import generate_randomkey
import urllib, urlparse

@login_manager.user_loader
def load_user(cwruID):
    """This function is required by Flask-Login.

    It uses the login manager's user_loader decorator.

    The purpose of this function is to return the User entity with the matching userid.

    :param userid: The unique user identifier. Currently this is a unicode version of the cwru ID
    :type userid: unicode

    :rtype: application.models.User
    """
    return getUsers(limit=1,cwruID=cwruID)[0]

def getUsers(limit=None,**kwargs):
    """This function takes the information in the kwargs dictionary
    and queries the datastore for the information. It returns the query results.

    If keys in kwargs don't match attributes of the User model then those keys are ignored

    If there are no kwargs then all Users will be returned.

    When limit is None all entities matching the query parameters will be returned.

    :param limit: This is the maximum number of users returned
    :type limit: int or None

    :param kwargs: Optional parameters that will be specified in the search
    :type kwargs: dict

    :rtype: list of application.models.User
    """
    if limit <= 0 and limit is not None:
        return []

    q = User.all()
    for key in kwargs:
        if(hasattr(User,key)): # only filter on valid attributes
            q.filter(key + ' =', kwargs[key])

    if(limit is None):
        limit = q.count()

    return q.fetch(limit)
    

def createUser(firstName, lastName, cwruID, password, middleName=None, contractType=None, family=None, big=None, avatar=None):
    """This function takes in information for a new user and creates a new user entity
    in the datastore. If the creation is successful it returns the User entity object
    just created. If the creation is not successful None is returned.

    :param firstName: First name of new user
    :type firstName: unicode

    :param lastName: Last name of new user
    :type lastName: unicode

    :param cwruID: CWRU ID of User
    :type cwruID: unicode

    :param password: Password of User
    :type password: unicode

    :param middleName: Middle Name of user - default: None
    :type middleName: unicode

    :param contractType: Contact Type of User - default: None
    :type contractType: application.models.Contract

    :param family: Family of User - default: None
    :type family: application.models.Family

    :param big: Big of User - default: None
    :type big: application.models.User

    :param avatar: Gravatar URL of user - default:None
    :type avatar: unicode

    :rtype: application.models.User or None
    """
    salt = generate_randomkey(256)
    hasher = SHA.new(salt +  password)
    newUser = User(firstName=firstName,
                   lastName=lastName,
                   cwruID=cwruID,
                   salt=salt,
                   hash=hasher.hexdigest(),
                   middleName=middleName,
                   contractType=contractType,
                   family=family,
                   big=big,
                   avatar=avatar)

    q = User.all()
    q.filter('cwruID =', cwruID)

    # make sure the cwruID's are unique
    if(q.count() == 1):
        return None
        
    try:
        newUser.put()
    except:
        return None
        
    return newUser

def deleteUser(cwruID):
    """Deletes the user specified by the cwruID

    Returns True if the deletion is a success
    Otherwise returns False
    
    :param cwruID: CWRU ID of the user
    :type cwruID: unicode

    :rtype: bool
    """
    q = User.all()
    q.filter('cwruID =', cwruID)

    if( q.count() == 0):
        return False
        
    result = q.fetch(1)

    result[0].delete()

    return True

def verifyLogin(cwruID, password):
    """Checks the user id and password combination

    Returns True if the password is valid
    Returns False otherwise

    :param cwruID: CWRU ID of user
    :type cwruID: unicode

    :param password: Password of user
    :type password: unicode

    :rtype: bool
    """
    q = User.all()
    q.filter('cwruID =', cwruID)

    if( q.count() == 0):
        return False

    user = q.fetch(1)[0]
        
    hasher = SHA.new(user.salt + password)
    if hasher.hexdigest() == user.hash:
        return True
    else:
        return False

def getAvatar(cwruID, host, size=100, default="/static/img/avatar.png"):
    """
    Looks up gravatar avatar url based on cwruID

    This code is based on the code at
    http://en.gravatar.com/site/implement/images/python/
    """

    q = User.all()
    q.filter('cwruID =', cwruID)

    if( q.count() == 0):
        return default

    user = q.fetch(1)[0]

    if user.avatar is None:
        return default
    
    email = user.avatar

    default = urlparse.urljoin(host, default)
    
    gravatar_url = "http://www.gravatar.com/avatar/" + MD5.new(email.lower()).hexdigest() + "?"
    gravatar_url += urllib.urlencode({'d':default, 's':str(size)})

    return gravatar_url