Member Profile Functional Tests
===============================

.. These allow the ID numbers to be relative to the overall test
   numbers in the entire document yet still be labeled starting from one on
   each page.

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

+---------------------------------------------------------------+
|Functional Test Requirements for REQ-16: Exec members shall be |
|able to create member profile types                            |
+---------------+---------------+---------------+---------------+
|ID             |Description    |Test Steps     |Expected       |
|               |               |               |Outcome        |
+===============+===============+===============+===============+
||1|            |Test if a non  |Step 1: Go to  |An error       |
|               |exec member can|login page and |message saying |
|               |create create  |login with     |that the user  |
|               |roles          |username       |doesn't have   |
|               |               |'zzz111' and   |permission to  |
|               |               |password       |access this    |
|               |               |'password'     |page should be |
|               |               |               |displayed.     |
|               |               |Step 2: Go to  |               |
|               |               |the create user|               |
|               |               |roles page.    |               |
+---------------+---------------+---------------+---------------+
||2|            |Test if an exec|Step 1: Go to  |A message      |
|               |member can     |the login page |saying the role|
|               |create         |and login with |was            |
|               |roles. Also    |username       |successfully   |
|               |tests          |'admin' and    |created should |
|               |requirement    |password       |be displayed   |
|               |**REQ-16.1:    |'password'     |               |
|               |Exec members   |               |               |
|               |shall be able  |Step 2: Go to  |               |
|               |to create      |the create user|               |
|               |member profile |roles page     |               |
|               |types**        |               |               |
|               |               |Step 3: Enter  |               |
|               |               |'test' into the|               |
|               |               |role name field|               |
|               |               |without the    |               |
|               |               |single-quotes  |               |
|               |               |               |               |
|               |               |Step 4: Enter  |               |
|               |               |'a role used   |               |
|               |               |for testing'   |               |
|               |               |into the role  |               |
|               |               |description    |               |
|               |               |field without  |               |
|               |               |the            |               |
|               |               |single-quotes  |               |
|               |               |               |               |
|               |               |Step 5: Click  |               |
|               |               |the create role|               |
|               |               |button         |               |
+---------------+---------------+---------------+---------------+
||3|            |Test if a role |Step 1: If test|An error       |
|               |can be used to ||2| has not    |message should |
|               |stop a user    |been completed,|be displayed   |
|               |from accessing |then complete  |stating that   |
|               |the page. Also |test |2|       |the user does  |
|               |tests.         |               |not have the   |
|               |**REQ-16.2:    |Step 2: Go to  |privileges to  |
|               |Exec members   |the page       |view this page.|
|               |shall be able  |permissions    |               |
|               |to assign page |page           |               |
|               |permission for |               |               |
|               |new profile    |Step 3: Select |               |
|               |type**         |the home page  |               |
|               |               |and the test   |               |
|               |               |role.          |               |
|               |               |               |               |
|               |               |Step 4: click  |               |
|               |               |the add        |               |
|               |               |permissions to |               |
|               |               |page button.   |               |
|               |               |               |               |
|               |               |Step 5: Go to  |               |
|               |               |the homepage.  |               |
+---------------+---------------+---------------+---------------+
||4|            |Tests if when  |Step 1: If test|The homepage   |
|               |the user has   ||3| has not    |should be      |
|               |the correct    |been complete  |successfully   |
|               |type the user  |then complete  |displayed      |
|               |can access the |test |3|       |               |
|               |page. Also     |               |               |
|               |tests.         |Step 2: Go to  |               |
|               |**REQ-16.2:    |the user roles |               |
|               |Exec members   |page           |               |
|               |shall be able  |               |               |
|               |to assign page |Step 3: Add the|               |
|               |permission for |test role      |               |
|               |new profile    |create in test |               |
|               |type**         |2 to the       |               |
|               |               |'admin' user   |               |
|               |               |               |               |
|               |               |Step 4: Go to  |               |
|               |               |the homepage.  |               |
+---------------+---------------+---------------+---------------+


+----------------------------------------------------------------+
|Functional Tests for REQ-17: Exec members shall be able to      |
|create new member accounts                                      |
+---------------+----------------+---------------+---------------+
|ID             |Description     |Test Steps     |Expected       |
|               |                |               |Outcome        |
+===============+================+===============+===============+
||5|            |Tests if REQ-17 |Step 1: Login  |All of the     |
|               |and all         |with test      |information    |
|               |sub-requirements|account        |entered on the |
|               |are satisfied   |username       |member creation|
|               |                |'admin' and    |page will be   |
|               |                |password       |displayed on   |
|               |                |'password'     |the new        |
|               |                |               |member's page  |
|               |                |Step 2: Go to  |               |
|               |                |the member     |               |
|               |                |creation page  |               |
|               |                |               |               |
|               |                |Step 3: Enter  |               |
|               |                |'test' for the |               |
|               |                |username       |               |
|               |                |               |               |
|               |                |Step 4: Enter a|               |
|               |                |first and last |               |
|               |                |name           |               |
|               |                |               |               |
|               |                |Step 5: Enter  |               |
|               |                |an address     |               |
|               |                |               |               |
|               |                |Step 6: Enter a|               |
|               |                |phone number   |               |
|               |                |               |               |
|               |                |Step 7: Enter a|               |
|               |                |gravatar email |               |
|               |                |in the profile |               |
|               |                |box            |               |
|               |                |               |               |
|               |                |Step 8: Click  |               |
|               |                |the create user|               |
|               |                |button.        |               |
|               |                |               |               |
|               |                |Step 9: Go to  |               |
|               |                |the all members|               |
|               |                |page           |               |
|               |                |               |               |
|               |                |Step 10: Find  |               |
|               |                |the newly      |               |
|               |                |created member |               |
|               |                |and click view |               |
|               |                |profile        |               |
|               |                |               |               |
|               |                |Step 11: Verify|               |
|               |                |that the       |               |
|               |                |information    |               |
|               |                |entered on the |               |
|               |                |member creation|               |
|               |                |page is the    |               |
|               |                |same           |               |
+---------------+----------------+---------------+---------------+

+---------------------------------------------------------------+
|Functional Tests for REQ-18: Exec members shall be able to     |
|delete member accounts                                         |
+---------------+---------------+---------------+---------------+
|ID             |Description    |Test Steps     |Expected       |
|               |               |               |Outcome        |
+===============+===============+===============+===============+
||6|            |Determine if a |Step 1: If test|User created in|
|               |user can be    ||5| has not    |test |5| no    |
|               |deleted        |been completed |longer shows up|
|               |               |then go and    |on all members |
|               |               |complete test  |page.          |
|               |               ||5|            |               |
|               |               |               |               |
|               |               |Step 2: Go to  |               |
|               |               |the all members|               |
|               |               |page           |               |
|               |               |               |               |
|               |               |Step 3: Find   |               |
|               |               |the user 'test'|               |
|               |               |created in test|               |
|               |               |5              |               |
|               |               |               |               |
|               |               |Step 4: Click  |               |
|               |               |the delete     |               |
|               |               |profile button |               |
|               |               |               |               |
|               |               |Step 5: Verify |               |
|               |               |that the member|               |
|               |               |'test' no      |               |
|               |               |longer shows up|               |
|               |               |on all members |               |
|               |               |page           |               |
+---------------+---------------+---------------+---------------+

+---------------------------------------------------------------+
|Functional Tests for REQ-19: Exec members shall be able to set |
|member profiles to an existing profile type                    |
+---------------+---------------+---------------+---------------+
|ID             |Description    |Test Steps     |Expected       |
|               |               |               |Outcome        |
+===============+===============+===============+===============+
||7|            |Determine if a |Step 1: Go to  |The user roles |
|               |new profile    |the roles page |page will show |
|               |type can be    |and verify that|that the       |
|               |assigned to an |the 'test' role|'admin' account|
|               |existing       |exists. If the |has a role of  |
|               |account        |role exists    |'test'         |
|               |               |continue to    |               |
|               |               |step           |               |
|               |               |2. Otherwise   |               |
|               |               |continue to    |               |
|               |               |Step 1a        |               |
|               |               |               |               |
|               |               |Step 1a: Go to |               |
|               |               |the create     |               |
|               |               |roles page     |               |
|               |               |               |               |
|               |               |Step 1b: Create|               |
|               |               |the role with  |               |
|               |               |name 'test' and|               |
|               |               |description    |               |
|               |               |'role for      |               |
|               |               |testing'       |               |
|               |               |               |               |
|               |               |Step 2: Go to  |               |
|               |               |the user roles |               |
|               |               |page           |               |
|               |               |               |               |
|               |               |Step 3: Find   |               |
|               |               |the currently  |               |
|               |               |logged in user |               |
|               |               |'admin'        |               |
|               |               |               |               |
|               |               |Step 4: Add the|               |
|               |               |test role to   |               |
|               |               |the user       |               |
|               |               |               |               |
|               |               |Step 5: Verify |               |
|               |               |that on the    |               |
|               |               |user roles page|               |
|               |               |the test role  |               |
|               |               |is assigned to |               |
|               |               |the admin      |               |
|               |               |account        |               |
+---------------+---------------+---------------+---------------+

+-----------------------------------------------------------------+
|Functional Tests REQ-20: Brothers and pledges shall be able to   |
|update the information in their profiles                         |
+---------------+-----------------+---------------+---------------+
|ID             |Description      |Test Steps     |Expected       |
|               |                 |               |Outcome        |
+===============+=================+===============+===============+
||8|            |Test if the user |Step 1: Login  |The information|
|               |can add and      |as 'test' with |on the member  |
|               |update their own |password       |profile page   |
|               |profile          |'password'     |should match   |
|               |information. Also|               |the information|
|               |tests all        |Step 1: Go to  |entered by the |
|               |sub-requirements |the all members|tester.        |
|               |of **REQ-20** and|page           |               |
|               |                 |               |               |
|               |                 |Step 2: Find   |               |
|               |                 |the currently  |               |
|               |                 |logged in      |               |
|               |                 |member 'test'  |               |
|               |                 |               |               |
|               |                 |Step 3: Click  |               |
|               |                 |on the edit    |               |
|               |                 |profile link   |               |
|               |                 |for the 'test' |               |
|               |                 |account        |               |
|               |                 |               |               |
|               |                 |Step 4: Change |               |
|               |                 |the first and  |               |
|               |                 |last name of   |               |
|               |                 |the user       |               |
|               |                 |               |               |
|               |                 |Step 5: Change |               |
|               |                 |the address of |               |
|               |                 |the user. If   |               |
|               |                 |the address    |               |
|               |                 |does not exist |               |
|               |                 |then create one|               |
|               |                 |               |               |
|               |                 |Step 6: Change |               |
|               |                 |the phone      |               |
|               |                 |number of the  |               |
|               |                 |user. If the   |               |
|               |                 |phone number   |               |
|               |                 |does not exist |               |
|               |                 |then create one|               |
|               |                 |               |               |
|               |                 |Step 7: Click  |               |
|               |                 |the save button|               |
|               |                 |               |               |
|               |                 |Step 8: Go back|               |
|               |                 |to the all     |               |
|               |                 |members        |               |
|               |                 |               |               |
|               |                 |Step 9: Find   |               |
|               |                 |the 'test'     |               |
|               |                 |member         |               |
|               |                 |               |               |
|               |                 |Step 10: Click |               |
|               |                 |on the view    |               |
|               |                 |link for the   |               |
|               |                 |'test' member  |               |
|               |                 |               |               |
|               |                 |Step 11: Verify|               |
|               |                 |that the       |               |
|               |                 |information    |               |
|               |                 |displayed      |               |
|               |                 |matches the    |               |
|               |                 |information    |               |
|               |                 |entered        |               |
+---------------+-----------------+---------------+---------------+


+----------------------------------------------------------------+
|Functional Tests for REQ-21: All members should be able to view |
|other member profiles                                           |
+---------------+----------------+---------------+---------------+
|ID             |Description     |Test Steps     |Expected       |
|               |                |               |Outcome        |
+===============+================+===============+===============+
||9|            |Test if a member|Step 1: Login  |All of the     |
|               |can see another |as the user    |information    |
|               |members         |'test' with the|listed in the  |
|               |profile. This   |password       |test is        |
|               |also tests all  |'password'     |displayed      |
|               |sub-requirements|               |               |
|               |of REQ-21       |Step 2: Go to  |               |
|               |                |the all members|               |
|               |                |page           |               |
|               |                |               |               |
|               |                |Step 3: Find   |               |
|               |                |the 'admin'    |               |
|               |                |account        |               |
|               |                |               |               |
|               |                |Step 4: Click  |               |
|               |                |on the view    |               |
|               |                |button for the |               |
|               |                |'admin' account|               |
|               |                |               |               |
|               |                |Step 5: Verify |               |
|               |                |that the user's|               |
|               |                |first and last |               |
|               |                |name is        |               |
|               |                |displayed.     |               |
|               |                |               |               |
|               |                |Step 6: Verify |               |
|               |                |that the user's|               |
|               |                |address is     |               |
|               |                |displayed      |               |
|               |                |               |               |
|               |                |Step 7: Verify |               |
|               |                |that the user's|               |
|               |                |phone number is|               |
|               |                |displayed      |               |
|               |                |               |               |
|               |                |Step 8: Verify |               |
|               |                |that the user's|               |
|               |                |profile picture|               |
|               |                |is displayed   |               |
+---------------+----------------+---------------+---------------+
