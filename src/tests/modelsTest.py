#!/usr/bin/nenv python
# encoding: utf-8
"""
modelsTest.py

This file contains the tests for the various models

"""
import unittest

from google.appengine.ext import db

from AppEngineTestCase import AppEngineTestCase as TestCase

from application import models

class FamilyModelTestCase(TestCase):

    def testAttributes(self):
        self.fail('Not Implemented!')

class ContractModelTestCase(TestCase):

    def testAttributes(self):
        self.fail('Not Implemented!')

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
        self.fail('Not Implemented!')

class UserRoleModelTestCase(TestCase):

    def testAttributes(self):
        self.fail('Not Implemented!')

class AddressModelTestCase(TestCase):

    def testAttributes(self):
        self.fail('Not Implemented!')

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
        