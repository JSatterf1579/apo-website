#!/usr/bin/nenv python
# encoding: utf-8
"""
accountsTest.py

Tis file contains tests for the functions and classes in the accounts module
"""
import unittest

from google.appengine.ext import db

from testHarness import AppEngineTestCase as TestCase

from application.models import User, Family
from application import accounts

class AccountsTestCase(TestCase):

    def createFakeUsers(self):
        # Create fake Families
        family1 = Family(name='Green')
        family2 = Family(name='Blue')

        # store the families
        family1.put()
        family2.put()

        # store the families for later use
        self.families = [family1, family2]
        
        # First create some fake users
        user1 = User(firstName='Darryl',
                     lastName='Gillmore',
                     cwruID='dag23',
                     salt='C7kzRIHPu2fE7NL28zJpMi42WbGO6zo5YEaaNawSGMssOQPfhMrhtiTFMBCOynBE24tPTV8aZZHAWFl52tIfR3Pa9YgVwpckzQw2A0rQ22LzcNZE700xWUx1aE8X5aPdjDezEyMyZiThTNJxcPruSN0Ddc7KZ3umuRgqx17TPNR4qR6zsNd2idee90xiAFZ5EWMc6xlQtLm2GAJpHDEg44yceADriVyWyGQHT6bnoXVZNp7kr3mANwNI1lPlddw1',
                     hash='ba46d29894dcde81c7f82a154df2d1584eef07f2',
                     family=family1)
        user1.put()
        
        user2 = User(firstName='Darryl',
                     lastName='Styer',
                     cwruID='dxs',
                     salt='GJnwtjTxGFjRIQKRwrehAB1owpPYfPUy0lhakpbHh1rv3J1LS8xcXFsJvj37Sy9U60CAMu8ejwnhjijt7jNUSG9W2YGw7SVPY56CVXezeeGJkaEh87p9LZ919Or5gnPiF8fXrs6CtjWJgbKQ7gZST91ZmSVfXYdeUs6iyspFdrpgDzU1LibBEC5NstMOx5GnV7L3tAAC5hsOTYWXEtd8S2XArex5XY5mHWesI7ZQ1HL4jfCQXY7xzzCsSs3hwmAh',
                     hash='2db50a4bab58562e1d9ec8ea2b68945fdf3c6f52',
                     family=family2)
        user2.put()
        
        user3 = User(firstName='Kurt',
                     lastName='Styer',
                     cwruID='kss3',
                     salt='LW2XN0UDzqd0QIMR4PbYKThNXVdC0Omr7BnGWZt7mVu8Igm7L2OSuQx8ry1WtVWKiN3jFcbx98s3vx18yiNYEo6zaoiVITp0AQx6ZIjNdJd9UBqNw79TS2Zj1Vd19AiPTIectwJfpQFec60JcJvoH9UfE4Lb6uLD9WwaBYf4Ty7AuIBXk5vgT5yv5CdRA2yFrfCxClX8nHqHGkLU8UtyOWRvDrWbwG6C4f08mo1OkNd3eT5d8YGlYONeQ9rqfcb6',
                     hash='9f2c76aa925cc16bff4a024e70d0c2286d4989e6',
                     family=family2,
                     big=user2)
        user3.put()
        
        user4 = User(firstName='Odessa',
                     lastName='Dietrich',
                     cwruID='ord5',
                     salt='Nzj3EO8WNtOC7tpLO5GkyCtpJoqDusINHvvRUWwhf8HekwhuiN1ig5dVOnGlfLIs4Umbdll1DbpfaclqXocD3cY0GqBBrnn0T02LrwKZLWR3NlnWShwxCzbRY2WkSl98eziUThhHakHpttvOJxy8zpV1x8jRaGyr1mX25bjjnKhPLS7Klk0D3w1AsAb0D7Q2Zw74P9CZYjN2EEacdv6QV2SmWDQgXKWGYMP2oEOeIu4l1gqxdcesYjC8HOrOz6Ym',
                     hash='ef5e2133bf7d9af575f18323f0b0ad9428dfa2da')
        user4.put()

        # store the users so the test methods can
        # compare the returned users with the
        # actual user
        self.users = [user1, user2, user3, user4]

    def test_getUser(self):
        # First create some fake users
        self.createFakeUsers()

        # Make sure nothing is returned if no matches
        users = accounts.getUsers(cwruID='111')
        self.assertIsNotNone(users, 'Users is None')
        self.assertEqual(len(users),0,
                         'There should be no users returned, however, %i were returned' % (len(users)))
        
        # See if the Users can be filtered by cwruID
        users = accounts.getUsers(cwruID='dxs')
        self.assertIsNotNone(users, 'Users is None')
        self.assertEqual(len(users), 1,
                         'There should only be 1 user returned, however, %i were returned' % (len(users)))

        self.assertIn(users[0], self.users)

        # See if User's can be filtered by lastName
        users = accounts.getUsers(lastName='Styer')
        self.assertIsNotNone(users, 'Users is None')
        self.assertEqual(len(users), 2,
                         'There should be 2 users returned, however, %i were returned' % (len(users)))

        
        self.assertIn(users[0], self.users)

        users = accounts.getUsers(firstName='Darryl')
        self.assertIsNotNone(users, 'Users is None')
        self.assertEqual(len(users), 2,
                         'There should be 2 users returned, however, %i were returned' % (len(users)))
        
        for user in users:
            self.assertIn(user, self.users)

        users = accounts.getUsers(firstName='Darryl',
                                 lastName='Styer')
        self.assertIsNotNone(users, 'Users is None')
        self.assertEqual(len(users), 1,
                         'There should be 1 user returned, however, %i were returned' % (len(users)))
        self.assertIn(users[0], self.users)
        
        # filter based on family
        users = accounts.getUsers(family=self.families[1])
        self.assertIsNotNone(users, 'Users is None')
        self.assertEqual(len(users), 2,
                         'There should be 2 users returned, however, %i were returned' % (len(users)))
        for user in users:
            self.assertIn(user, self.users)

        # Test if limit works
        users = accounts.getUsers(limit=1, lastName='Styer')
        self.assertIsNotNone(users, 'Users is None')
        self.assertEqual(len(users), 1, 'There should be 1 user returned, however, %i were returned' % len(users))

        # Test if limit works
        users = accounts.getUsers(limit=5, lastName='Styer')
        self.assertIsNotNone(users, 'Users is None')
        self.assertEqual(len(users), 2, 'There should be 2 users returned, however, %i were returned' % len(users))

        # Test if adding nonexistent fields causes problems
        users = accounts.getUsers(fake='test')
        self.assertIsNotNone(users, 'Users is None')
        self.assertEqual(len(users), 4, 'There should be 4 users returned, however, %i were returned' % len(users))

        # Test if no arguments gives all users
        users = accounts.getUsers()
        self.assertIsNotNone(users, 'Users is None')
        self.assertEqual(len(users), 4, 'There should be 4 users returned, however, %i were returned' % len(users))



    def test_createUser(self):
        # First create a user with only the default arguments
        newUser = accounts.createUser('Rand', 'AlThor', 'rxa1', 'No1secret!')

        # Make sure that cwruID is kept unique
        duplicateUser = accounts.createUser('Randy', 'AlThor', 'rxa1', 'No1secret!')

        # make sure a user was actually created
        self.assertIsNotNone(newUser, 'User was not successfully created')

        # make sure the second attempt failed
        self.assertIsNone(duplicateUser, 'duplicateUser should be None')

        # query for the user to make sure it was actually added
        q = User.all()
        q.filter('cwruID =', 'rxa1')

        results = q.fetch(q.count())

        self.assertEqual( len(results), 1, 'Expected a single User be returned from the datastore. However, %i users were returned.' % (len(results)) )

        # Make sure the returned user matches the input data
        self.assertEqual(results[0].firstName, newUser.firstName)
        self.assertEqual(results[0].lastName, newUser.lastName)
        self.assertEqual(results[0].cwruID, newUser.cwruID)
        self.assertIsNone(results[0].middleName)
        self.assertIsNone(results[0].contractType)
        self.assertIsNone(results[0].family)
        self.assertIsNone(results[0].big)
        self.assertIsNone(results[0].avatar)
        

    def test_deleteUser(self):
        self.createFakeUsers()

        success = accounts.deleteUser(self.users[0].cwruID)
        self.assertTrue(success, 'Failed to delete user %s' % self.users[0].cwruID)

        success = accounts.deleteUser('111')
        self.assertFalse(success, 'Deleted a user that should not exist')

    def test_verifyLogin(self):
        # Test with valid passwords
        self.createFakeUsers()
        for i,user in enumerate(self.users):
            success = accounts.verifyLogin(user.cwruID, 'password%i' % (i+1))
            self.assertTrue(success,
                            'Login invalid for user %s with password %s' % (user.cwruID, 'password%i' % (i+1)))

        # Test with invalid passwords
        success = accounts.verifyLogin(self.users[0].cwruID, 'wrong!')
        self.assertFalse(success, 'Valid login for user %s with wrong password' % self.users[0].cwruID)

        # Test with invalid cwruIDs
        success = accounts.verifyLogin('111', 'wrong!')
        self.assertFalse(success, 'Valid login for nonexistant user')
            
if __name__ == '__main__':
    unittest.main()