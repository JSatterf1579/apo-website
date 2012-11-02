#!/usr/bin/nenv python
# encoding: utf-8
"""This module contains the unit tests for the methods and functions in the
accounts.accounts package

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""
import sys, os

sys.path.insert(0, os.path.abspath('../../'))

print sys.path

import unittest

from google.appengine.ext import db

from tests.testHarness import AppEngineTestCase as TestCase

import application.accounts.accounts as accounts

class CreateUserTestCase(TestCase): # pylint: disable=R0904
    """This class tests the create_user function
    in the accounts.accounts module"""
    
    def test_missing_arguments(self):
        """This method tests whether the create_user
        function actually requires the right number of
        arguments"""
        
        try:
            accounts.create_user() # pylint: disable=E1120
            self.fail('Should have thrown a TypeError ' +
                      'becuase create_user requires at least' +
                      '4 arguments')
        except TypeError, error:
            self.assertEqual(error.message,
                             'create_user() takes exactly 4 ' +
                             'arguments (0 given)')

    def test_kwargs(self):
        """This method tests whether the create_user
        function will accept kwargs"""
        
        new_user = accounts.create_user('John',
                                      'Schmidt',
                                      'jjs11',
                                      'password',
                                      mname='Jacob Jinglehiemer')
        self.assertEqual(new_user._User__UserModel.mname, # pylint: disable=W0212,C0301
                         'Jacob Jinglehiemer')

    def test_ignore_nonexistant_kwargs(self):
        """This method tests whether the create_user
        function will ignore kwarg keys that don't
        actually exist in the user model"""
        
        new_user = accounts.create_user('John',
                                      'Schmidt',
                                      'jjs11',
                                      'password',
                                      fake='fake')

        try:
            new_user.fake # pylint: disable=W0104,E1101
            self.fail('Should have thrown an AttributeError')
        except AttributeError:
            pass

    def test_error_on_nonmodifiable_kwargs(self):
        """This method tests whether the create_user
        function will throw an error when a nonmodifiable
        field of kwargs is tried to be set via the kwargs
        dictionary"""
        try:
            accounts.create_user('John',
                                 'Schmidt',
                                 'jjs11',
                                 'password',
                                 hash='hash')
            self.fail('Should have thrown a BadValueError')
        except AttributeError:
            pass

    def test_error_on_invalid_kwargs(self):
        """This method tests whether the create_user
        function will error like its supposed to when
        an invalid type for one of the kwargs is passed
        in"""
        
        try:
            accounts.create_user('John',
                                'Schmidt',
                                'jjs11',
                                'password',
                                mname=55)
            self.fail('Should have thrown a BadValueError')
        except db.BadValueError:
            pass

    def test_non_unique_cwruid(self):
        """This method tests whether the create_user
        function will throw an error upon trying
        to create a user with a duplicate cwruID"""
        
        accounts.create_user('John',
                            'Smith',
                            'jxs11',
                            'password')

        try:
            accounts.create_user('John',
                                'Smith',
                                'jxs11',
                                'password')
            self.fail('Should have thrown an AttributeError ' +
                      'because cwruid must be unique')
        except AttributeError:
            pass

class UserTestCase(TestCase): # pylint: disable=R0904
    """This class contains methods that
    test the User class in the accounts.accounts
    module"""
    
    def setUp(self): # pylint: disable=C0103,C0111
        # do the normal setup
        super(UserTestCase, self).setUp()

        # create an instance of the User object
        self.user = accounts.create_user('John',
                                        'Smith',
                                        'jxs11',
                                        'password')
        
    def test_attributes(self):
        """This method verifies that the __User
        class as the attributes specified in the design
        docs"""
        
        # check if there is an internal __User
        self.assertTrue(hasattr(self.user, '_User__UserModel'),
                        'User class has no internal __UserModel attribute')

if __name__ == '__main__':
    unittest.main()