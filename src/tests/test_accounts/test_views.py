"""This module contains the tests for the views in the
account package

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

import sys, os

if os.path.abspath('../../') not in sys.path:
    sys.path.insert(0, os.path.abspath('../../'))

import unittest
from tests.testHarness import AppEngineTestCase as TestCase

from flask import url_for

from flaskext.flask_login import login_user, login_required, logout_user, current_user

from application import app

import application.accounts.accounts as accounts


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


class LoginTestCase(TestCase):

    def setUp(self):
        # do the normal setUp
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
        app.add_url_rule('/secretTest', 'secret', self.secret)

        # redo the test client
        self.app = app.test_client()

        # make the fake users
        self.users = create_test_users()

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def login(self, username, password):
        return self.app.post('/login', data=dict(cwruid=username,
                                                 password=password),
                             follow_redirects=True)

    def test_access_denied(self):
        # Make sure that brand new user is denied access
        # to login required pages
        rv  = self.app.get('/secretTest')
        self.assertNotIn("Shhh! It's a secret!", rv.data, "client wasn't denied access to /secretTest")

        rv = self.app.get('/secretTest', follow_redirects=True)
        self.assertIn("Login", rv.data, "Client wasn't redirected to login page")

    def test_login(self):
        # Test logging in with incorrect username
        rv = self.login('111','password1')
        self.assertNotIn('Success', rv.data, "Login was successful with incorrect username")
        
        # Test logging in with incorrect password
        rv = self.login('sxm1','wrong!')
        self.assertNotIn('Success', rv.data, "Login was successful with incorrect password")
        
        # Test logging in with correct username and password
        rv = self.login('sxm1', 'password')
        self.assertIn('Success', rv.data)

        rv = self.app.get('/secretTest')
        self.assertIn("Shhh! It's a secret!", rv.data, "Client was denied access to /secretTest")

    def test_logout(self):
        # login
        rv = self.login('sxm1', 'password')
        self.assertIn('Success', rv.data)

        # logout
        rv = self.logout()

        rv = self.app.get('/secretTest')
        self.assertNotIn("Shhh! It's a secret!", rv.data, "Client wasn't denied access to /secretTest")
    def test_redirect(self):
        rv = self.app.post('/login?next=%2FsecretTest',
                          data = dict(cwruid='sxm1',
                                      password='password'),
                          follow_redirects=True)
        self.assertIn("Shhh! It's a secret!", rv.data)
        

if __name__ == "__main__":
    unittest.main()
