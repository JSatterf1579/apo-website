#!/usr/bin/nenv python
# encoding: utf-8
"""
modelsTest.py

This file contains the tests for the various models

"""
import unittest
import datetime

from google.appengine.ext import testbed
from google.appengine.ext import db

from application import models

class EventModelTestCase(unittest.TestCase):
    def setUp(self):
        # setup app engine test bed
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_user_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def testInsertAndQueryEntity(self):
        event = models.Event(name='test',
                             date=datetime.date(1991,9,18),
                             startTime=datetime.time(),
                             endTime=datetime.time())

        event.put()

        # Check if all the fields that are supposed to be required are implemented
        try:
            event = models.Event(date=datetime.date(1991,9,18),
                             startTime=datetime.time(),
                             endTime=datetime.time())
            self.fail('name field is not required but it should be')
        except db.BadValueError:
            pass
        try:
            event = models.Event(name='test',
                             startTime=datetime.time(),
                             endTime=datetime.time())
            self.fail('date field is not required but it should be')
        except db.BadValueError:
            pass
        try:
            event = models.Event(name='test',
                             date=datetime.date(1991,9,18),
                             endTime=datetime.time())
            self.fail('startTime field is not required but it should be')
        except db.BadValueError:
            pass
        try:
            event = models.Event(name='test',
                             date=datetime.date(1991,9,18),
                             startTime=datetime.time())
            self.fail('endTime field is not required but it should be')
        except db.BadValueError:
            pass
            
        q = models.Event.all()

        if q.count() != 1:
            self.fail('There should be one and only one result')

if __name__ == '__main__':
    unittest.main()
        