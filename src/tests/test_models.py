#!/usr/bin/nenv python
# encoding: utf-8
"""
modelsTest.py

This file contains the tests for the various models

"""
import unittest

from google.appengine.ext import db

from testHarness import AppEngineTestCase as TestCase

from application import models

class FamilyModelTestCase(TestCase):

    def testAttributes(self):
        # Check if attributes exist
        self.assertTrue(hasattr(models.Family, 'name'), 'Family model has no name attribute')

        # Check type of attributes
        self.assertTrue(isinstance(models.Family.name, db.StringProperty), 'Family.name should be a unicode string')

        # Check if required attributes are required
        self.assertTrue(models.Family.name.required, 'Family.name should be required')

class ContractModelTestCase(TestCase):

    def testAttributes(self):
        # Check if attributes exist
        self.assertTrue(hasattr(models.Contract, 'name'), 'Contract model has no name attribute')

        # Check type of attributes
        self.assertTrue(isinstance(models.Contract.name, db.StringProperty), 'Contract.name should be a unicode string')

        # Check if required attributes are required
        self.assertTrue(models.Contract.name.required, 'Contract.name should be required')

class UserModelTestCase(TestCase):

    def testAttributes(self):
        # Check if attributes exist
        self.assertTrue(hasattr(models.User,'firstName'), 'User model has no firstName attribute')
        self.assertTrue(hasattr(models.User,'lastName'), 'User model has no lastName attribute')
        self.assertTrue(hasattr(models.User,'cwruID'), 'User model has no cwruID attribute')
        self.assertTrue(hasattr(models.User,'salt'), 'User model has no salt attribute')
        self.assertTrue(hasattr(models.User,'hash'), 'User model has no hash attribute')
        self.assertTrue(hasattr(models.User,'middleName'), 'User model has no middleName attribute')
        self.assertTrue(hasattr(models.User,'contractType'), 'User model has no contractType attribute')
        self.assertTrue(hasattr(models.User,'family'), 'User model has no family attribute')
        self.assertTrue(hasattr(models.User,'big'), 'User model has no big attribute')
        self.assertTrue(hasattr(models.User,'avatar'), 'User model has no avatar attribute')

        # Check type of attributes
        self.assertTrue(isinstance(models.User.firstName, db.StringProperty), 'User.firstName should be a unicode string')
        self.assertTrue(isinstance(models.User.lastName, db.StringProperty), 'User.lastName should be a unicode string')
        self.assertTrue(isinstance(models.User.cwruID, db.StringProperty), 'User.cwruID should be a unicode string')
        self.assertTrue(isinstance(models.User.salt, db.StringProperty), 'User.salt should be a unicode string')
        self.assertTrue(isinstance(models.User.hash, db.StringProperty), 'User.hash should be a unicode string')
        self.assertTrue(isinstance(models.User.middleName, db.StringProperty), 'User.middleName should be a unicode string')
        self.assertTrue(isinstance(models.User.contractType, db.ReferenceProperty), 'User.contractType should be a reference to a Contract entity')
        self.assertTrue(isinstance(models.User.family, db.ReferenceProperty), 'User.family should be a reference to a Family entity')
        self.assertTrue(isinstance(models.User.big, db.ReferenceProperty), 'User.big should be a self reference')
        self.assertTrue(isinstance(models.User.avatar, db.StringProperty), 'User.avatar should be a unicode string')

        # Check if required attributes are required
        self.assertTrue(models.User.firstName.required, 'User.firstName should be required')
        self.assertTrue(models.User.lastName.required, 'User.lastName should be required')
        self.assertTrue(models.User.cwruID.required, 'User.cwruID should be required')
        self.assertTrue(models.User.salt.required, 'User.salt should be required')
        self.assertTrue(models.User.hash.required, 'User.hash should be required')

        # Check if optional attributes are optional
        self.assertFalse(models.User.middleName.required, 'User.middleName should be optional')
        self.assertFalse(models.User.contractType.required, 'User.contractType should be optional')
        self.assertFalse(models.User.family.required, 'User.family should be optional')
        self.assertFalse(models.User.big.required, 'User.big should be optional')
        self.assertFalse(models.User.avatar.required, 'User.avatar should be optional')

class RoleModelTestCase(TestCase):

    def testAttributes(self):
        # Check if attributes exist
        self.assertTrue(hasattr(models.Role, 'name'), 'Role model has no name attribute')
        self.assertTrue(hasattr(models.Role, 'desc'), 'Role model has no desc attribute')

        # Check if attributes are correct type
        self.assertTrue(isinstance(models.Role.name, db.StringProperty), 'Role.name should be a unicode string')
        self.assertTrue(isinstance(models.Role.desc, db.StringProperty), 'Role.desc should be a unicode string')

        # Check if required attributes are required
        self.assertTrue(models.Role.name.required, 'Role.name should be required')

        # Check if optional attributes are optional
        self.assertFalse(models.Role.desc.required, 'Role.desc should be optional')

class UserRoleModelTestCase(TestCase):

    def testAttributes(self):
        # Check if attributes exist
        self.assertTrue(hasattr(models.UserRole, 'user'), 'UserRole model has no user attribute')
        self.assertTrue(hasattr(models.UserRole, 'role'), 'UserRole model has no role attribute')

        # Check if attributes are correct type
        self.assertTrue(isinstance(models.UserRole.user, db.ReferenceProperty), 'UserRole.user should be a reference to a User entity')
        self.assertTrue(isinstance(models.UserRole.role, db.ReferenceProperty), 'UserRole.role should be a reference to a Role entity')

        # Check if required attributes are required
        self.assertTrue(models.UserRole.user.required, 'UserRole.user should be required')
        self.assertTrue(models.UserRole.role.required, 'UserRole.role should be required')

class AddressModelTestCase(TestCase):

    def testAttributes(self):
        # Check if attributes exist
        self.assertTrue(hasattr(models.Address, 'user'), 'Address model has no user attribute')
        self.assertTrue(hasattr(models.Address, 'address'), 'Address model has no address attribute')
        self.assertTrue(hasattr(models.Address, 'name'), 'Address model has no name attribute')

        # Check if attributes are correct type
        self.assertTrue(isinstance(models.Address.user, db.ReferenceProperty), 'Address.user should be a reference to a User entity')
        self.assertTrue(isinstance(models.Address.address, db.PostalAddressProperty), 'Address.address should be a PostalAddress entity')
        self.assertTrue(isinstance(models.Address.name, db.StringProperty), 'Address.name should be a unicode string')

        # Check if required attributes are required
        self.assertTrue(models.Address.user.required, 'Address.user should be required')
        self.assertTrue(models.Address.address.required, 'Address.address should be required')

        # Check if optional attributes are optional
        self.assertFalse(models.Address.name.required, 'Address.name should be optional')

class EmailModelTestCase(TestCase):

    def testAttributes(self):
        self.fail('Not Implemented!')

class PhoneNumberModelTestCase(TestCase):

    def testAttributes(self):
        self.fail('Not Implemented!')

class EventModelTestCase(TestCase):

    def testAttributes(self):
        self.fail('Not Implemented!')

class LocationModelTestCase(TestCase):
   
    def testAttributes(self):
        pass

class ServiceEventModelTestCase(TestCase):
    def testAttributes(self):
        self.fail('Not implemented!')

class ServiceSignUpModelTestCase(TestCase):

    def testAttributes(self):
        self.fail('Not Implemented!')

class InsideServiceReportModelTestCase(TestCase):

    def testAttributes(self):
        self.fail('Not Implemented!')

class OutsideServiceReportModelTestCase(TestCase):

    def testAttributes(self):
        self.fail('Not Implemented!')

class ServiceHourModelTestCase(TestCase):

    def testAttributes(self):
        self.fail('Not Implemented!')

class ChapterEventModelTestCase(TestCase):

    def testAttributes(self):
        self.fail('Not Implemented!')

class RequirementModelTestCase(TestCase):

    def testAttributes(self):
        self.fail('Not Implemented!')

class HourReqModelTestCase(TestCase):

    def testAttributes(self):
        self.fail('Not Implemented!')

class DuesReqModelTestCase(TestCase):

    def testAttributes(self):
        self.fail('Not Implemented!')

class AttendanceModelTestCase(TestCase):

    def testAttributes(self):
        self.fail('Not Implemented!')

class PostModelTestCase(TestCase):

    def testAttributes(self):
        self.fail('Not Implemented!')

class CommentModelTestCase(TestCase):

    def testAttributes(self):
        self.fail('Not Implemented!')
        
if __name__ == '__main__':
    unittest.main()
        