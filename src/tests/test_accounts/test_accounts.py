#!/usr/bin/nenv python
# encoding: utf-8
"""This module contains the unit tests for the methods and functions in the
accounts.accounts package

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""
import sys, os

if os.path.abspath('../../') not in sys.path:
    sys.path.insert(0, os.path.abspath('../../'))

import unittest

from tests.harness import AppEngineTestCase as TestCase

import application.accounts.accounts as accounts

from nose.tools import nottest

@nottest
def create_test_users():
    # create some test users
    users = []
    users.append(accounts.create_user('Eric',
                                      'Cartman',
                                      'exc',
                                      'password'))
    users.append(accounts.create_user('Randy',
                                      'Marsh',
                                      'rxm',
                                      'password'))
    users.append(accounts.create_user('Stan',
                                      'Marsh',
                                      'sxm1',
                                      'password',
                                      big=users[1].key()))
    users.append(accounts.create_user('Kyle',
                                      'Broflovski',
                                      'kxb1',
                                      'password'))

    return users

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

    def test_error_on_nonmod_kwargs(self):
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
            self.fail('Should have thrown an AttributeError')
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
            self.fail('Should have thrown an AttributeError')
        except AttributeError:
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

class FindUsersTestCase(TestCase): # pylint: disable=R0904
    """This class contains methods that
    test the application.accounts.accounts.find_users
    method"""

    def setUp(self): # pylint: disable=C0103
        """This method calls the normal
        setUp method provided by the AppEngineTestCase.
        It also sets up multiple test users that
        are queried against to test the find_users
        method"""
        # do the normal setup
        super(FindUsersTestCase, self).setUp()

        self.users = create_test_users()

    def test_return_all_users(self):
        """This method tests whether find_users
        will return all users with no parameters
        """
        users = accounts.find_users()

        self.assertEqual(len(users), 4)

        for user in users:
            self.assertIn(user, self.users)

    def test_return_limited(self):
        """This method tests whether the find_users
        will return a limited amount of users
        when limit is specified
        """
        users = accounts.find_users(1)

        self.assertEqual(len(users), 1)

        self.assertIn(users[0], self.users)

    def test_return_big_limit(self):
        """This method tests whether if limit
        is bigger than the total number of users
        that all users will be returned"""
        users = accounts.find_users(10)

        self.assertEqual(len(users), 4)

    def test_return_cwruid_match(self):
        """This method tests whether the find_users
        method will return the user matching the
        cwruid specified
        """
        users = accounts.find_users(cwruid=('=','rxm'))

        self.assertEqual(len(users), 1)

        self.assertEqual(users[0], self.users[1])

    def test_return_multiple_match(self):
        """This method tests whether multiple
        users will be returned when multiple
        users are matched
        """
        users = accounts.find_users(lname=('=','Marsh'))

        self.assertEqual(len(users), 2)

        for user in users:
            self.assertIn(user, self.users[1:3])

    def test_invalid_queries(self):
        """This method tests whether errors
        are raised when invalid queries are
        issued"""

        try:
            accounts.find_users(fake=('=','fake'))
            self.fail("Should have raised an error")
        except AttributeError:
            pass

        try:
            accounts.find_users(limit=-1)
            self.fail("Should have raised an error")
        except TypeError:
            pass

        try:
            accounts.find_users(lname=('='))
            self.fail("Should have raised an error")
        except TypeError:
            pass

                          
class UserTestCase(TestCase): # pylint: disable=R0904
    """This class contains methods that
    test the User class in the accounts.accounts
    module"""
    
    def setUp(self): # pylint: disable=C0103,C0111
        # do the normal setup
        super(UserTestCase, self).setUp()

        # create test users
        self.users = create_test_users()
        
    def test_attributes(self):
        """This method verifies that the User
        class as the attributes specified in the design
        docs"""
        user = accounts.find_users(limit=1)[0]
        # check if there is an internal __User
        self.assertTrue(hasattr(user, '_User__UserModel'),
                        'User class has no internal __UserModel attribute')

    def test_save(self):
        """This method verifies that the save
        method on the User class updates the
        attributes in the datastore
        """
        testid = 'sxm1'
        user = accounts.find_users(cwruid=('=', testid))[0]

        user.fname = 'Stanley'

        self.assertEqual(user.fname, u'Stanley')
        self.assertEqual(user._User__UserModel.fname, u'Stan')

        user.save()

        self.assertEqual(user.fname, 'Stanley')
        self.assertEqual(user._User__UserModel.fname, 'Stanley')

    def test_equal(self):
        """This method verifies that the __eq__
        method works properly"""
        testid = 'sxm1'
        user1 = accounts.find_users(cwruid=('=', testid))[0]

        user2 = accounts.find_users(cwruid=('=', testid))[0]

        self.assertEqual(user1, user2)

    def test_not_equal(self):
        """This method verifies that when not equal
        __eq__ returns false"""
        testid = 'sxm1'
        user1 = accounts.find_users(cwruid=('=', testid))[0]

        user2 = accounts.find_users(cwruid=('=', 'exc'))[0]

        self.assertNotEqual(user1, user2)

    def test_equal_wrong_obj(self):
        """This method verifies that an AttributeError
        is thrown when equal is compared with the wrong type"""
        testid = 'sxm1'
        user1 = accounts.find_users(cwruid=('=', testid))[0]

        class Fake(object):
            pass

        fake = Fake()
        
        self.assertFalse(user1 == fake)


    def test_delete(self):
        """This method verifies that the
        delete method on the User class
        updates the users in the datastore
        """
        testid = 'sxm1'
        user1 = accounts.find_users(cwruid=('=', testid))[0]

        user1.delete()

        user2 = accounts.find_users(cwruid=('=', testid))

        self.assertEqual(len(user2), 0)

    def test_getattr_nochanges(self):
        """This method verifies that the
        __getattribute__ method will
        return the value of the corresponding
        attribute of internal User Model
        instance
        """
        testid = 'sxm1'
        user = accounts.find_users(cwruid=('=', testid))[0]
        self.assertEqual(user.cwruid, testid)

    def test_getattr_changes(self):
        """This method verifies that the
        __getattribute__ method will
        return the value that is
        pending"""
        testid = 'sxm1'
        user = accounts.find_users(cwruid=('=', testid))[0]
        user.fname = 'Stanley'

        olduser = accounts.find_users(cwruid=('=', testid))[0]
        self.assertEqual(user.fname, 'Stanley')
        self.assertEqual(olduser.fname, 'Stan')

    def test_getattr_noexist(self):
        """This method verifies that the
        __getattribute__ method will
        raise an AttributeError if the
        request attribute doesn't exist"""
        testid = 'sxm1'
        user = accounts.find_users(cwruid=('=', testid))[0]

        try:
            user.fake
            self.fail('Should have raised an AttributeError')
        except AttributeError:
            pass

    def test_getattr_noaccess(self):
        """This method verifies that the
        __getattribute__ method will
        raise an AttributeError if the request
        attribute is marked as non accessible in
        the User class"""
        testid = 'sxm1'
        user = accounts.find_users(cwruid=('=', testid))[0]

        try:
            user.hash
            self.fail('Should have raised an AttributeError')
        except AttributeError:
            pass

    def test_setattr(self):
        """This method verifies that the
        __setattr__ method will
        set a pending change on a valid
        attribute name"""
        testid = 'sxm1'
        user = accounts.find_users(cwruid=('=', testid))[0]

        user.fname='Stanley'

    def test_setattr_noexist(self):
        """This method verifies that the
        __setattr__ method will
        raise an AttributeError when
        the attribute being set
        doesn't exist"""
        testid = 'sxm1'
        user = accounts.find_users(cwruid=('=', testid))[0]

        try:
            user.fake = 'fake'
            self.fail('Should raise an AttributeError')
        except AttributeError:
            pass
            
    def test_setattr_nomod(self):
        """This method verifies that the
        __setattr__ method will
        not modify values marked as no
        modify in the User class
        """
        testid = 'sxm1'
        user = accounts.find_users(cwruid=('=', testid))[0]

        try:
            user.cwruid = 'cwruid'
            self.fail('Should raise an AttributeError')
        except AttributeError:
            pass
        except:
            self.fail()

    def test_set_new_password(self):
        """This method verifies that the
        set_new_password method works
        properly"""
        testid = 'sxm1'
        user = accounts.find_users(cwruid=('=', testid))[0]

        self.assertTrue(user.valid_password('password'))

        user.set_new_password('newpassword')

        self.assertFalse(user.valid_password('password'))
        self.assertTrue(user.valid_password('newpassword'))

    def test_valid_password(self):
        """This method verifies that the
        check_password method works
        properly"""
        testid = 'sxm1'
        user = accounts.find_users(cwruid=('=', testid))[0]

        self.assertTrue(user.valid_password('password'))
        self.assertFalse(user.valid_password('wrong'))

    def test_rollback_all(self):
        """This method verifies that the
        rollback method will rollback
        all pending changes when no names
        are specified"""
        testid = 'sxm1'
        user = accounts.find_users(cwruid=('=', testid))[0]

        # make some changes
        user.fname = 'Stanley'
        user.lname = 'March'

        self.assertEqual(user.fname, u'Stanley')
        self.assertEqual(user.lname, u'March')

        user.rollback()

        self.assertEqual(user.fname, u'Stan')
        self.assertEqual(user.lname, u'Marsh')

    def test_rollback_multi(self):
        """This method verifies that the
        rollback method will rollback
        multiple pending parameters
        """
        testid = 'sxm1'
        user = accounts.find_users(cwruid=('=', testid))[0]

        # set some "mistakes"
        user.fname = 'Stanley'
        user.lname = 'March'
        user.big = self.users[0].key()

        self.assertEqual(user.fname, u'Stanley')
        self.assertEqual(user.lname, u'March')
        self.assertEqual(user.big, self.users[0].key())

        user.rollback('lname', 'big')

        self.assertEqual(user.fname, u'Stanley')
        self.assertEqual(user.lname, u'Marsh')
        self.assertEqual(user.big.key(), self.users[1].key())

    def test_key(self):
        """This method verifies that the
        key method will return a key value
        """
        testid = 'sxm1'
        user = accounts.find_users(cwruid=('=', testid))[0]

        key = user.key()

        self.assertIsNotNone(key)

    def test_get_id(self):
        """This method verifies that the
        get_id method returns the cwruid
        of the user"""
        testid = 'sxm1'
        user = accounts.find_users(cwruid=('=', testid))[0]

        self.assertEqual(user.get_id(), user.cwruid)
        

if __name__ == '__main__':
    unittest.main()