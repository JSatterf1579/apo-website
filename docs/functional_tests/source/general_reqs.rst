General Requirements Functional Tests
=====================================




+-----+-----------+-----------+--------------+-------------+
|Test |Requirement|Description|Test          |Expected     |
|ID   |           |           |Steps         |Result       |
+-----+-----------+-----------+--------------+-------------+
|1    |REQ-1      |Test that a|Step 1: Go to |User         |
|     |           |user can't |the login page|denied       |
|     |           |login with |              |access and   |
|     |           |incorrect  |Step 2: Type  |error        |
|     |           |username   |in the        |message is   |
|     |           |           |username      |displayed    |
|     |           |           |'incorrect'   |             |
|     |           |           |without the   |             |
|     |           |           |single-quotes.|             |
|     |           |           |              |             |
|     |           |           |Step 3: Type  |             |
|     |           |           |in the        |             |
|     |           |           |password      |             |
|     |           |           |'password'    |             |
|     |           |           |without the   |             |
|     |           |           |single-quotes |             |
|     |           |           |              |             |
|     |           |           |Step 4: Click |             |
|     |           |           |the login     |             |
|     |           |           |button        |             |
|     |           |           |              |             |
|     |           |           |              |             |
+-----+-----------+-----------+--------------+-------------+
|2    |REQ-1      |Test that a|Step          |User         |
|     |           |user can't |1: Go         |denied       |
|     |           |login with |to            |access and   |
|     |           |incorrect  |the           |error        |
|     |           |password   |login         |message is   |
|     |           |           |page          |displayed    |
|     |           |           |              |             |
|     |           |           |Step 2: Type  |             |
|     |           |           |in the        |             |
|     |           |           |username      |             |
|     |           |           |'zzz111'      |             |
|     |           |           |without the   |             |
|     |           |           |single-quotes.|             |
|     |           |           |              |             |
|     |           |           |Step 3: Type  |             |
|     |           |           |in the        |             |
|     |           |           |password      |             |
|     |           |           |'incorrect'   |             |
|     |           |           |without the   |             |
|     |           |           |single-quotes.|             |
|     |           |           |              |             |
|     |           |           |Step 4:       |             |
|     |           |           |Click the     |             |
|     |           |           |login button  |             |
|     |           |           |              |             |
|     |           |           |              |             |
+-----+-----------+-----------+--------------+-------------+
|3    |REQ-1      |Test that a|Step          |A message    |
|     |           |user can   |1: Go         |saying the   |
|     |           |login with |to            |user has     |
|     |           |correct    |the           |successfully |
|     |           |username   |login         |logged in is |
|     |           |and        |page          |displayed.   |
|     |           |password   |              |             |
|     |           |           |Step 2: Type  |             |
|     |           |           |in the        |             |
|     |           |           |username      |             |
|     |           |           |'zzz111'      |             |
|     |           |           |without the   |             |
|     |           |           |single-quotes.|             |
|     |           |           |              |             |
|     |           |           |Step 3: Type  |             |
|     |           |           |in the        |             |
|     |           |           |password      |             |
|     |           |           |'password'    |             |
|     |           |           |without the   |             |
|     |           |           |single-quotes.|             |
|     |           |           |              |             |
|     |           |           |Step 4: Click |             |
|     |           |           |on the login  |             |
|     |           |           |button        |             |
+-----+-----------+-----------+--------------+-------------+
|4    |REQ-1.1    |Test that  |Step          |Error message|
|     |           |passwords  |1: Go         |about        |
|     |           |less than 8|to the        |password     |
|     |           |characters |create        |length is    |
|     |           |are        |a user        |displayed and|
|     |           |rejected   |page          |user is not  |
|     |           |           |              |created      |
|     |           |           |Step 2: Type  |             |
|     |           |           |in the        |             |
|     |           |           |username      |             |
|     |           |           |'zzz222'      |             |
|     |           |           |without the   |             |
|     |           |           |single-quotes |             |
|     |           |           |              |             |
|     |           |           |Step 3: Type  |             |
|     |           |           |in the        |             |
|     |           |           |password 'a'  |             |
|     |           |           |without the   |             |
|     |           |           |single-quotes.|             |
|     |           |           |              |             |
|     |           |           |Step 4: Click |             |
|     |           |           |on the create |             |
|     |           |           |user button   |             |
+-----+-----------+-----------+--------------+-------------+
|5    |REQ-1.1    |Test that  |Step          |Message      |
|     |           |passwords 8|1: Go         |saying       |
|     |           |characters |to the        |user was     |
|     |           |or longer  |create        |created      |
|     |           |are        |a user        |is           |
|     |           |accepted   |page          |displayed    |
|     |           |           |              |             |
|     |           |           |Step 2: Type  |             |
|     |           |           |in the        |             |
|     |           |           |username      |             |
|     |           |           |'zzz222'      |             |
|     |           |           |without the   |             |
|     |           |           |single-quotes |             |
|     |           |           |              |             |
|     |           |           |Step 3: Type  |             |
|     |           |           |in the        |             |
|     |           |           |password      |             |
|     |           |           |'password1@'  |             |
|     |           |           |              |             |
|     |           |           |Step 4: Click |             |
|     |           |           |on the create |             |
|     |           |           |user button.  |             |
+-----+-----------+-----------+--------------+-------------+
|6    |REQ-1.2    |Test that  |Step 1: Go to |The first    |
|     |           |duplicate  |the create a  |user is      |
|     |           |users can't|user page     |created, but |
|     |           |be created |              |the second   |
|     |           |           |Step 2: Type  |user causes  |
|     |           |           |in the        |an error     |
|     |           |           |username      |message to be|
|     |           |           |'zzz333'      |displayed and|
|     |           |           |without the   |is not       |
|     |           |           |single-quotes |created.     |
|     |           |           |              |             |
|     |           |           |Step 3: Type  |             |
|     |           |           |in the        |             |
|     |           |           |password      |             |
|     |           |           |'password1@'  |             |
|     |           |           |              |             |
|     |           |           |Step 4: Click |             |
|     |           |           |on the create |             |
|     |           |           |user button.  |             |
|     |           |           |              |             |
|     |           |           |Step 5: Go to |             |
|     |           |           |the create a  |             |
|     |           |           |user page     |             |
|     |           |           |              |             |
|     |           |           |Step 6: Type  |             |
|     |           |           |in the        |             |
|     |           |           |username      |             |
|     |           |           |'zzz333'      |             |
|     |           |           |without the   |             |
|     |           |           |single-quotes |             |
|     |           |           |              |             |
|     |           |           |Step 7: Type  |             |
|     |           |           |in the        |             |
|     |           |           |password      |             |
|     |           |           |'password2@'  |             |
|     |           |           |              |             |
|     |           |           |Step 8: Click |             |
|     |           |           |on the create |             |
|     |           |           |user button.  |             |
+-----+-----------+-----------+--------------+-------------+
