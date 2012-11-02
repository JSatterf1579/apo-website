#!/usr/bin/nenv python
# encoding: utf-8
"""This module contains the unit tests for the methods
and functions in the accounts.models package

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

import sys, os

if os.path.abspath('../../') not in sys.path:
    sys.path.insert(0, os.path.abspath('../../'))

import unittest

from tests.testHarness import AppEngineTestCase as TestCase

from google.appengine.ext import db

import application.accounts.models as models

class UserModelTestCase(TestCase):
    """This class tests the UserModel
    class in the accounts.models module"""

    def test_attributes_present(self):
        """This method verifies
        that the attributes specified
        in the design doc are contained
        within the UserModel class
        """
        # Make sure all of the attributes are present
        self.assertTrue(hasattr(models.UserModel, 'fname'))
        self.assertTrue(hasattr(models.UserModel, 'lname'))
        self.assertTrue(hasattr(models.UserModel, 'cwruid'))
        self.assertTrue(hasattr(models.UserModel, 'salt'))
        self.assertTrue(hasattr(models.UserModel, 'hash'))
        self.assertTrue(hasattr(models.UserModel, 'mname'))
        self.assertTrue(hasattr(models.UserModel, 'contract_type'))
        self.assertTrue(hasattr(models.UserModel, 'family'))
        self.assertTrue(hasattr(models.UserModel, 'big'))
        self.assertTrue(hasattr(models.UserModel, 'avatar'))        

    def test_required_attr(self):
        """This method verifies that the attributes
        specified as required in the design doc
        are specified as required in the UserModel
        class
        """
        # Make sure all of the required attributes are required
        self.assertTrue(models.UserModel.fname.required)
        self.assertTrue(models.UserModel.lname.required)
        self.assertTrue(models.UserModel.cwruid.required)
        self.assertTrue(models.UserModel.salt.required)
        self.assertTrue(models.UserModel.hash.required)

    def test_optional_attr(self):
        """This method verifies that the attributes
        specified as optional in the design doc are
        specified as optional in the UserModel class
        """
        # Make sure the optional attributes are required
        self.assertFalse(models.UserModel.mname.required)
        self.assertFalse(models.UserModel.contract_type.required)
        self.assertFalse(models.UserModel.family.required)
        self.assertFalse(models.UserModel.big.required)
        self.assertFalse(models.UserModel.avatar.required)

    def test_attr_type(self):
        """This method verifies that the attributes
        of the UserModel match the types specified
        in the design doc
        """
        self.assertTrue(isinstance(models.UserModel.fname, db.StringProperty))
        self.assertTrue(isinstance(models.UserModel.lname, db.StringProperty))
        self.assertTrue(isinstance(models.UserModel.cwruid, db.StringProperty))
        self.assertTrue(isinstance(models.UserModel.salt, db.StringProperty))
        self.assertTrue(isinstance(models.UserModel.hash, db.StringProperty))
        self.assertTrue(isinstance(models.UserModel.mname, db.StringProperty))
        self.assertTrue(isinstance(models.UserModel.contract_type, db.ReferenceProperty))
        self.assertTrue(isinstance(models.UserModel.family, db.ReferenceProperty))
        self.assertTrue(isinstance(models.UserModel.big, db.ReferenceProperty))
        self.assertTrue(isinstance(models.UserModel.avatar, db.StringProperty))        

class RoleModelTestCase(TestCase):

    def test_attributes_present(self):
        self.assertTrue(hasattr(models.RoleModel, 'name'))
        self.assertTrue(hasattr(models.RoleModel, 'desc'))

    def test_attr_type(self):
        self.assertTrue(isinstance(models.RoleModel.name, db.StringProperty))
        self.assertTrue(isinstance(models.RoleModel.desc, db.StringProperty))

    def test_required_attr(self):
        self.assertTrue(models.RoleModel.name.required)
        self.assertTrue(models.RoleModel.desc.required)

class UserRoleModelTestCase(TestCase):

    def test_attributes_present(self):
        self.assertTrue(hasattr(models.UserRoleModel, 'user'))
        self.assertTrue(hasattr(models.UserRoleModel, 'role'))

    def test_attr_type(self):
        self.assertTrue(isinstance(models.UserRoleModel.user, db.ReferenceProperty))
        self.assertTrue(isinstance(models.UserRoleModel.role, db.ReferenceProperty))

    def test_required_attr(self):
        self.assertTrue(models.UserRoleModel.user.required)
        self.assertTrue(models.UserRoleModel.role.required)
        
if __name__ == '__main__':
    unittest.main()