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
                             endTime=datetime.time(),
                             description='test description')

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

        result = q.fetch(1)[0]
        # Make sure the returned results match
        self.assertEqual(result.name, 'test')
        self.assertEqual(result.date, datetime.date(1991, 9, 18))
        self.assertEqual(result.startTime, datetime.time())
        self.assertEqual(result.endTime, datetime.time())
        self.assertEqual(result.description, 'test description')


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
                             endTime=datetime.time(),
                             description='test description')
        event.put()
        location = models.Location(name='Village House 3a Rm 142b',
                                   event=event.key(),
                                   address=db.PostalAddress('1681 E 116th St., Cleveland, OH 44106'))

        location.put()

        try:
           models.Location(event=event.key(),
                           address=db.PostalAddress('1681 E 116th St., Cleveland, OH 44106'))
           self.fail('name field is not required but it should be')
        except db.BadValueError:
            pass

        try:
            models.Location(name='Village House 3a Rm 142b',
                                   address=db.PostalAddress('1681 E 116th St., Cleveland, OH 44106'))
            self.fail('event field is not required but it should be')
        except db.BadValueError:
            pass

        q = models.Location.all()

        if q.count() != 1:
            self.fail('Should only be 1 location in the datastore but there are %i' % count(q))

        result = q.fetch(1)[0]
        self.assertEqual(result.name,'Village House 3a Rm 142b')
        self.assertEqual(result.event.key(),event.key())
        self.assertEqual(result.address,db.PostalAddress('1681 E 116th St., Cleveland, OH 44106'))

        
        
if __name__ == '__main__':
    unittest.main()
        