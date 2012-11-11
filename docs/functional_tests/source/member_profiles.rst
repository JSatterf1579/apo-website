Member Profile Functional Tests
===============================

+---------------------------------------------------------------+
|Functional Test Requirements for REQ-16: Exec members shall be |
|able to create member profile types                            |
+---------------+---------------+---------------+---------------+
|ID             |Description    |Test Steps     |Expected       |
|               |               |               |Outcome        |
+===============+===============+===============+===============+
|1              |Test if a non  |Step 1: Go to  |An error       |
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
|2              |Test if an exec|Step 1: Go to  |A message      |
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
|3              |Test if a role |Step 1: If test|An error       |
|               |can be used to |2 has not been |message should |
|               |stop a user    |completed, then|be displayed   |
|               |from accessing |complete test 2|stating that   |
|               |the page. Also |               |the user does  |
|               |tests.         |Step 2: Go to  |not have the   |
|               |**REQ-16.2:    |the page       |privileges to  |
|               |Exec members   |permissions    |view this page.|
|               |shall be able  |page           |               |
|               |to assign page |               |               |
|               |permission for |Step 3: Select |               |
|               |new profile    |the home page  |               |
|               |type**         |and the test   |               |
|               |               |role.          |               |
|               |               |               |               |
|               |               |Step 4: click  |               |
|               |               |the add        |               |
|               |               |permissions to |               |
|               |               |page button.   |               |
|               |               |               |               |
|               |               |Step 5: Go to  |               |
|               |               |the homepage.  |               |
|               |               |               |               |
+---------------+---------------+---------------+---------------+
|4              |Tests if when  |Step 1: If test|The homepage   |
|               |the user has   |3 has not been |should be      |
|               |the correct    |complete then  |successfully   |
|               |type the user  |complete test 3|displayed      |
|               |can access the |               |               |
|               |page. Also     |Step 2: Go to  |               |
|               |tests.         |the user roles |               |
|               |**REQ-16.2:    |page           |               |
|               |Exec members   |               |               |
|               |shall be able  |Step 3: Add the|               |
|               |to assign page |test role      |               |
|               |permission for |create in test |               |
|               |new profile    |2 to the       |               |
|               |type**         |'admin' user   |               |
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
|5              |Tests if REQ-17 |Step 1: Login  |All of the     |
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
|6              |Determine if a |Step 1: If test|User created in|
|               |user can be    |5 has not been |test 5 no      |
|               |deleted        |completed then |longer shows up|
|               |               |go and complete|on all members |
|               |               |test 5         |page.          |
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
|7              |Determine if a |Step 1: Go to  |The user roles |
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
|8              |Test if the user |Step 1: Login  |The information|
|               |can add and      |as 'test' with |on the member  |
|               |update their own |password       |profile page   |
|               |profile          |'password'     |should match   |
|               |information. Also|               |the information|
|               |tests all        |Step 1: Go to  |entered by the |
|               |sub-requirements |the all members|tester.        |
|               |of **REQ-20** and|page           |               |
|               |**REQ-21**       |               |               |
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
|               |                 |'admin' member |               |
|               |                 |               |               |
|               |                 |Step 11: Verify|               |
|               |                 |that the       |               |
|               |                 |information    |               |
|               |                 |displayed      |               |
|               |                 |matches the    |               |
|               |                 |information    |               |
|               |                 |entered        |               |
+---------------+-----------------+---------------+---------------+


