Service Events Functional Tests
===============================

.. |1| replace:: 1
.. |2| replace:: 2
.. |3| replace:: 3
.. |4| replace:: 4
.. |5| replace:: 5
.. |6| replace:: 6
.. |7| replace:: 7
.. |8| replace:: 8
.. |9| replace:: 9
.. |10| replace:: 10
.. |11| replace:: 11
.. |12| replace:: 12
.. |13| replace:: 13


+---------------------------------------------------------------+
|Functional Tests for REQ-2: Exec members shall be able to      |
|create a service event                                         |
+---------------+---------------+---------------+---------------+
|ID             |Description    |Test Steps     |Expected       |
|               |               |               |Outcome        |
+===============+===============+===============+===============+
||1|            |Test if a non  |Step 1: Go to  |An error       |
|               |exec member can|the login page |message saying |
|               |create a       |and login with |that the user  |
|               |service event  |username       |doesn't have   |
|               |               |'zzz111' and   |permission to  |
|               |               |password       |access this    |
|               |               |'password'     |page should be |
|               |               |               |displayed      |
|               |               |Step 2: Go to  |               |
|               |               |the create     |               |
|               |               |service event  |               |
|               |               |page           |               |
+---------------+---------------+---------------+---------------+
||2|            |Test if an exec|Step 1: Got to |A message      |
|               |member can     |the login page |saying the     |
|               |create a       |and login with |event was      |
|               |service        |username       |successfully   |
|               |event. Tests   |'admin' and    |created should |
|               |REQ-2.1 through|password       |be displayed   |
|               |REQ-2.6        |'password'     |               |
|               |               |               |               |
|               |               |Step 2: Enter a|               |
|               |               |date in the    |               |
|               |               |proper format  |               |
|               |               |to the date    |               |
|               |               |field          |               |
|               |               |               |               |
|               |               |Step 3: Enter a|               |
|               |               |time in the    |               |
|               |               |proper format  |               |
|               |               |to the time    |               |
|               |               |field          |               |
|               |               |               |               |
|               |               |Step 4: Enter a|               |
|               |               |location in the|               |
|               |               |proper format  |               |
|               |               |to the location|               |
|               |               |field          |               |
|               |               |               |               |
|               |               |Step 5: Enter  |               |
|               |               |any event      |               |
|               |               |description in |               |
|               |               |the description|               |
|               |               |field          |               |
|               |               |               |               |
|               |               |Step 6: Enter  |               |
|               |               |any number in  |               |
|               |               |the max        |               |
|               |               |brothers field |               |
|               |               |               |               |
|               |               |Step 7: Enter  |               |
|               |               |any text in the|               |
|               |               |additional     |               |
|               |               |infor field    |               |
|               |               |               |               |
|               |               |Step 8: Click  |               |
|               |               |the create     |               |
|               |               |event button   |               |
+---------------+---------------+---------------+---------------+

+---------------------------------------------------------------+
|Functional Test REQ-3: Exec members shall be able to update    |
|existing service events                                        |
+---------------+---------------+---------------+---------------+
|ID             |Description    |Test Steps     |Expected       |
|               |               |               |Outcome        |
+===============+===============+===============+===============+
||3|            |Test if a non  |Step 1: Go to  |An error       |
|               |exec member can|the login page |message saying |
|               |update a       |and login with |that the user  |
|               |service event  |username       |doesn't have   |
|               |               |'zzz111' and   |permission to  |
|               |               |password       |access this    |
|               |               |'password'     |page should be |
|               |               |               |displayed      |
|               |               |Step 2: Go to  |               |
|               |               |the update     |               |
|               |               |service event  |               |
|               |               |page           |               |
+---------------+---------------+---------------+---------------+
||4|            |Test if an exec|Step 1: Go to  |A message      |
|               |member can     |the login page |saying the     |
|               |update a       |and login with |event was      |
|               |service        |username       |successfully   |
|               |event. Tests   |'admin' and    |updated should |
|               |requirements   |password       |be             |
|               |REQ-3.1 through|'password'     |displayed. If  |
|               |REQ-3.6        |               |the event is   |
|               |               |Step 2: Select |viewed again   |
|               |               |an existing    |then the date, |
|               |               |service event. |time, event,   |
|               |               |               |max brothers   |
|               |               |Step 3: Change |and additional |
|               |               |the date       |info should    |
|               |               |               |match the data |
|               |               |Step 4: Change |entered.       |
|               |               |the time field |               |
|               |               |               |               |
|               |               |Step 5: Change |               |
|               |               |the event      |               |
|               |               |description    |               |
|               |               |               |               |
|               |               |Step 6: Change |               |
|               |               |the max        |               |
|               |               |brothers value |               |
|               |               |               |               |
|               |               |Step 7: Change |               |
|               |               |the additional |               |
|               |               |info field     |               |
|               |               |               |               |
|               |               |Step 8: Click  |               |
|               |               |the update     |               |
|               |               |event button   |               |
+---------------+---------------+---------------+---------------+


+---------------------------------------------------------------+
|Functional Test REQ-4: Brothers and pledges shall be able to   |
|view existing service events                                   |
+---------------+---------------+---------------+---------------+
|ID             |Description    |Test Steps     |Expected       |
|               |               |               |Outcome        |
+===============+===============+===============+===============+
||5|            |Test if a non  |Step 1: Log out|An error       |
|               |member can view|if already     |message saying |
|               |a service event|logged in      |that the user  |
|               |               |               |doesn't have   |
|               |               |Step 2: Go to  |permission to  |
|               |               |the view       |access this    |
|               |               |service event  |page should be |
|               |               |page           |displayed      |
+---------------+---------------+---------------+---------------+
||6|            |Test if a      |Step 1: Go to  |Date, time,    |
|               |member can view|the login page |location, event|
|               |the service    |and login with |description,   |
|               |event          |the username   |maximum number |
|               |page. Tests    |'zzz111' and   |of brothers,   |
|               |requirements   |password       |and additional |
|               |REQ-4.1 through|'password'     |info should be |
|               |REQ-4.6        |               |visible for    |
|               |               |Step 2: Go to  |selected event |
|               |               |the view       |               |
|               |               |service events |               |
|               |               |page           |               |
|               |               |               |               |
|               |               |Step 3: Click  |               |
|               |               |an event from  |               |
|               |               |the event list |               |
+---------------+---------------+---------------+---------------+

+---------------------------------------------------------------+
|Functional Test REQ-5: Brothers and pledges shall be able to   |
|update their responses to the additional information requested |
+---------------+---------------+---------------+---------------+
|ID             |Description    |Test Steps     |Expected       |
|               |               |               |Outcome        |
+===============+===============+===============+===============+
||7|            |Test if a      |Step 1: Go to  |A message      |
|               |member can     |the login page |saying the     |
|               |update the     |and login with |information was|
|               |additiona info |username       |successfully   |
|               |field          |'zzz111' and   |updated should |
|               |               |password       |be displayed   |
|               |               |'password'     |               |
|               |               |               |               |
|               |               |Step 2: Go to  |               |
|               |               |the view       |               |
|               |               |service event  |               |
|               |               |page           |               |
|               |               |               |               |
|               |               |Step 3: Click  |               |
|               |               |an event from  |               |
|               |               |the event list |               |
|               |               |               |               |
|               |               |Step 4: Enter  |               |
|               |               |text to the    |               |
|               |               |additional info|               |
|               |               |field          |               |
|               |               |               |               |
|               |               |Step 5: Click  |               |
|               |               |the submit     |               |
|               |               |additional info|               |
|               |               |button         |               |
+---------------+---------------+---------------+---------------+


+---------------------------------------------------------------+
|Functional Tests REQ-6: Brothers and pledges shall be able to  |
|join existing service events                                   |
+---------------+---------------+---------------+---------------+
|ID             |Description    |Test Steps     |Expected       |
|               |               |               |Outcome        |
+===============+===============+===============+===============+
||8|            |Test if a      |Step 1: Go to  |A message      |
|               |member can join|the login page |saying the     |
|               |an existing    |and login with |member has     |
|               |service event  |username       |successfully   |
|               |               |'zzz111' and   |joined the     |
|               |               |password       |service event  |
|               |               |'password'     |should be      |
|               |               |               |displayed. The |
|               |               |Step 2: Go to  |user should now|
|               |               |the view       |appear on the  |
|               |               |service event  |service event  |
|               |               |page           |page.          |
|               |               |               |               |
|               |               |Step 3: Click  |               |
|               |               |an event from  |               |
|               |               |the event list |               |
|               |               |               |               |
|               |               |Step 4: Click  |               |
|               |               |the sign up    |               |
|               |               |button         |               |
+---------------+---------------+---------------+---------------+


+---------------------------------------------------------------+
|Functional Tests REQ-7: Brothers and pledges shall be able to  |
|report service hours for a service event                       |
+---------------+---------------+---------------+---------------+
|ID             |Description    |Test Steps     |Expected       |
|               |               |               |Outcome        |
+===============+===============+===============+===============+
||9|            |Test is a      |Step 1: Go to  |A message      |
|               |member can     |the login page |saying that the|
|               |report service |and login with |hours have     |
|               |hours for a    |username       |successfully   |
|               |service        |'zzz111' and   |been reported  |
|               |event. tests   |password       |is displayed   |
|               |requirements   |'password'     |               |
|               |REQ-7.1 through|               |               |
|               |REQ-7.2        |Step 2: Go to  |               |
|               |               |the view       |               |
|               |               |service event  |               |
|               |               |page           |               |
|               |               |               |               |
|               |               |Step 3: Click  |               |
|               |               |an event from  |               |
|               |               |the event list |               |
|               |               |               |               |
|               |               |Step 4: Click  |               |
|               |               |the report     |               |
|               |               |hours button   |               |
|               |               |               |               |
|               |               |Step 5: Enter a|               |
|               |               |name in the    |               |
|               |               |name field     |               |
|               |               |               |               |
|               |               |Step 6: Enter a|               |
|               |               |number in the  |               |
|               |               |hours field    |               |
|               |               |               |               |
|               |               |Step 7: Click  |               |
|               |               |the submit     |               |
|               |               |hours button   |               |
+---------------+---------------+---------------+---------------+


+---------------------------------------------------------------+
|Functional Tests REQ-8: Exec members shall be able to approve  |
|submitted service hours                                        |
+---------------+---------------+---------------+---------------+
|ID             |Description    |Test Steps     |Expected       |
|               |               |               |Outcome        |
+===============+===============+===============+===============+
||10|           |Test if a non  |Step 1: Go to  |There should be|
|               |exec member can|the login page |no approve     |
|               |approve service|and login with |hours button   |
|               |hours          |username       |visible        |
|               |               |'zzz111' and   |               |
|               |               |password       |               |
|               |               |'password'     |               |
|               |               |               |               |
|               |               |Step 2: Go to  |               |
|               |               |the service    |               |
|               |               |event page     |               |
|               |               |               |               |
|               |               |Step 3: Click  |               |
|               |               |an event from  |               |
|               |               |the event list |               |
|               |               |               |               |
+---------------+---------------+---------------+---------------+
||11|           |Test if an exec|Step 1: Go to  |Any members    |
|               |member can view|the login page |signed up for  |
|               |submitted      |and login with |an event and   |
|               |service        |username       |their          |
|               |hours. Tests   |'admin' and    |corresponding  |
|               |requirements   |password       |hours should be|
|               |REQ-8.1 through|'password'     |visible        |
|               |REQ-8.2        |               |               |
|               |               |Step 2: Go to  |               |
|               |               |the view       |               |
|               |               |service event  |               |
|               |               |page           |               |
|               |               |               |               |
|               |               |Step 3: Click  |               |
|               |               |an event from  |               |
|               |               |teh event list |               |
|               |               |               |               |
|               |               |Step 4: Click  |               |
|               |               |on the approve |               |
|               |               |hours button   |               |
+---------------+---------------+---------------+---------------+
||12|           |Test if an exec|Step 1: Go to  |A message      |
|               |member can     |the login page |saying that the|
|               |approve        |and login with |hours have been|
|               |submitted      |username       |approved. On   |
|               |service        |'admin' and    |the service    |
|               |hours. Tests   |password       |event page the |
|               |REQ-8.3        |'password'     |hours will be  |
|               |               |               |listed as      |
|               |               |Step 2: Go to  |approved.      |
|               |               |the view       |               |
|               |               |service event  |               |
|               |               |page           |               |
|               |               |               |               |
|               |               |Step 3: Click  |               |
|               |               |an event from  |               |
|               |               |the event list |               |
|               |               |               |               |
|               |               |Step 4: Click  |               |
|               |               |on the approve |               |
|               |               |hours button   |               |
|               |               |               |               |
|               |               |Step 5: Click  |               |
|               |               |on the approve |               |
|               |               |button         |               |
+---------------+---------------+---------------+---------------+
||13|           |Test if an exec|Step 1: Go to  |A message      |
|               |member can     |the login page |saying that the|
|               |reject         |and login with |hours have been|
|               |submitted      |username       |rejected. On   |
|               |service        |'admin' and    |the service    |
|               |hours. Tests   |password       |event page the |
|               |requirement    |'password'     |hours will be  |
|               |REQ-8.3        |               |listed as      |
|               |               |Step 2: Go to  |rejected.      |
|               |               |the view       |               |
|               |               |service event  |               |
|               |               |page           |               |
|               |               |               |               |
|               |               |Step 3: Click  |               |
|               |               |an event from  |               |
|               |               |the event list |               |
|               |               |               |               |
|               |               |Step 4: Click  |               |
|               |               |on the approve |               |
|               |               |hours button   |               |
|               |               |               |               |
|               |               |Step 5: Click  |               |
|               |               |on the reject  |               |
|               |               |button         |               |
+---------------+---------------+---------------+---------------+



