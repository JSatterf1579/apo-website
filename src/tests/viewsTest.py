#!/usr/bin/nenv python
# encoding: utf-8
"""

viewsTest.py

This file contains tests for the views in the views.py module
"""
import unittest

from testHarness import AppEngineTestCase as TestCase
from flaskext.flask_login import login_user, login_required, logout_user, current_user

from application import app, accounts

from flask import url_for, redirect

class LoginTestCase(TestCase):

    def setUp(self):
        # do the normal setup
        super(LoginTestCase, self).setUp()

        app.config['TESTING'] = True
        app.config['CSRF_ENABLED'] = False
        
        # Setup a test view
        @login_required
        def secret():
            """Temporary secret page"""
            return "Shhh! It's a secret!"

        # add the test view
        self.secret = secret
        app.add_url_rule('/secretTest','secret',self.secret)

        # redo the test client
        self.app = app.test_client()

        # make the fake users
        self.createFakeUsers()

    def createFakeUsers(self):
        from application.models import Family, User
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

    
    def test_AccessDenied(self):
        # Make sure that brand new user is denied access
        # to login required pages
        rv  = self.app.get('/secretTest')
        self.assertNotIn("Shhh! It's a secret!", rv.data, "client wasn't denied login to /secretTest")

        rv = self.app.get('/secretTest', follow_redirects=True)
        self.assertIn("Login", rv.data, "Client wasn't redirected to login page")

    def test_login(self):
        self.fail('Not Implemented')

    def test_logout(self):
        self.fail('Not Implemented')

if __name__ == "__main__":
    unittest.main()