#!/usr/bin/nenv python
# encoding: utf-8
"""This module contains the unit tests for the methods
and classes in the accounts.forms package

.. moduleauthor:: Devin Schwab <dts34@case.edu>
"""

import sys, os

if os.path.abspath('../../') not in sys.path:
    sys.path.insert(0, os.path.abspath('../../'))

import unittest

from tests.harness import AppEngineTestCase as TestCase

import application.accounts.forms as forms

from flaskext import wtf
from flaskext.wtf import validators

class LogInFormTestCase(TestCase):

    def test_attributes_present(self):
        self.assertTrue(hasattr(forms.LoginForm, 'cwruid'))
        self.assertTrue(hasattr(forms.LoginForm, 'password'))

    def test_attr_type(self):
        self.assertEqual(forms.LoginForm.cwruid.field_class.__name__,
                         'TextField')
        self.assertEqual(forms.LoginForm.password.field_class.__name__,
                         'PasswordField')

class UpdatePasswordForm(wtf.Form):

    def test_attributes_present(self):
        self.assertTrue(hasattr(forms.LoginForm, 'old_password'))
        self.assertTrue(hasattr(forms.LoginForm, 'new_password'))
        self.assertTrue(hasattr(forms.LoginForm, 'confirm_password'))

    def test_attr_type(self):
        self.assertEqual(forms.LoginForm.old_password.field_class.__name__,
                         'PasswordField')
        self.assertEqual(forms.LoginForm.new_password.field_class.__name__,
                         'PasswordField')
        self.assertEqual(forms.LoginForm.confirm_password.field_class.__name__,
                         'PasswordField')

if __name__ == '__main__':
    unittest.main()