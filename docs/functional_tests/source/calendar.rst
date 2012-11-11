Calendar Functional Tests
=========================

.. |1| replace:: 1
.. |2| replace:: 2

Google Calendar is an excellent online calendar providing all of the required
features and more. Because the website will already
be running on Google App Engine a Google calendar account will automatically exist.
For these reasons Google Calendar will be used to meet all of the Calendar requirements.


+-------------------------------------------------------------------------+
|Functional Tests for REQ-22 through 26 including all                     |
|subrequirements                                                          |
+---------------+---------------+-------------------------+---------------+
|ID             |Description    |Test Steps               |Expected       |
|               |               |                         |Outcome        |
+---------------+---------------+-------------------------+---------------+
||1|            |Test if an     |Step 1: Go to            |Viewing the    |
|               |event can be   |www.google.com/ and click|calendar on the|
|               |created via    |on sign in               |website        |
|               |Google Calendar|                         |calendar page  |
|               |website        |Step 2: Login with the   |will display   |
|               |               |apo-cwru account         |the            |
|               |               |                         |event. Viewing |
|               |               |Step 3: Go to            |the event on   |
|               |               |google.com/calendar      |the calendar   |
|               |               |                         |will show the  |
|               |               |Step 4: Add an event to  |entered        |
|               |               |the calendar             |location,      |
|               |               |                         |description,   |
|               |               |Step 4a: Add a           |and notes      |
|               |               |description for the event|               |
|               |               |                         |               |
|               |               |Step 4b: Add a location  |               |
|               |               |for the event            |               |
|               |               |                         |               |
|               |               |Step 4c: Add additional  |               |
|               |               |information in the notes |               |
|               |               |section                  |               |
|               |               |                         |               |
|               |               |Step 5: Go to the        |               |
|               |               |calendar page on the     |               |
|               |               |website.                 |               |
|               |               |                         |               |
|               |               |Step 6: Verify that the  |               |
|               |               |event is displayed on the|               |
|               |               |calendar                 |               |
|               |               |                         |               |
|               |               |Step 7: Verify that the  |               |
|               |               |location is the location |               |
|               |               |entered                  |               |
|               |               |                         |               |
|               |               |Step 8: Verify that the  |               |
|               |               |description is the       |               |
|               |               |description entered      |               |
|               |               |                         |               |
|               |               |Step 9: Verify that the  |               |
|               |               |notes are the notes      |               |
|               |               |entered.                 |               |
+---------------+---------------+-------------------------+---------------+


