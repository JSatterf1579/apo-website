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



