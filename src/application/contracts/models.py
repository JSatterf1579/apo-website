"""
This module contains the models used by the
contracts package
"""

from application.accounts.models import UserModel

from google.appengine.ext import db
from google.appengine.ext.db.polymodel import PolyModel

import datetime as dt

class ContractModel(db.Model):
    """
    Models a contract which is a conglomeration
    of Requirements (ReqModel)
    """
    name = db.StringProperty(required=True)
    desc = db.StringProperty()

class ReqModel(PolyModel):
    """
    Models an abstract requirements.
    This is never actually used, only the
    subclasses are
    """
    name = db.StringProperty(required=True)
    contract_ = db.ReferenceProperty(ContractModel, required=True)
    dueDate = db.DateProperty(required=True)

class TimeReqModel(ReqModel):
    time = db.TimeProperty(required=True)

class DuesReqModel(ReqModel):
    amount = db.FloatProperty(required=True)

class AttendanceReqModel(ReqModel):
    amount = db.IntegerProperty(required=True)

class SignedContractModel(db.Model):
    """
    Models a user signing a contract
    """
    user = db.ReferenceProperty(UserModel, required=True)
    contract_ = db.ReferenceProperty(ContractModel, required=True)

class ReqProgressModel(PolyModel):
    """
    Models a users progress in a contract requirement
    """
    user = db.ReferenceProperty(UserModel, required=True)

class TimeReqProgressModel(ReqProgressModel):
    time = db.TimeProperty(required=True, default=dt.time())
    req = db.ReferenceProperty(TimeReqModel, required=True)
    
class DuesReqProgressModel(ReqProgressModel):
    amount = db.FloatProperty(required=True, default=0.0)
    req = db.ReferenceProperty(DuesReqModel, required=True)    

class AttendanceReqProgressModel(ReqProgressModel):
    amount = db.IntegerProperty(required=True, default=0)
    req = db.ReferenceProperty(AttendanceReqModel, required=True)    