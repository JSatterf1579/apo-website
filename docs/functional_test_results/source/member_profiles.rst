Member Profile Functional Test Results
======================================

+---------------+-------------------+---------------+
|ID             |Result             |Status         |
+---------------+-------------------+---------------+
|32             |No link to         |PASS           |
|               |create roles is    |               |
|               |displayed          |               |
+---------------+-------------------+---------------+
|33             |No link to         |FAIL           |
|               |create roles is    |               |
|               |displayed          |               |
+---------------+-------------------+---------------+
|34             |No link to page    |FAIL           |
|               |permissions        |               |
|               |displayed. However,|               |
|               |pages are          |               |
|               |restricted based on|               |
|               |existing roles     |               |
+---------------+-------------------+---------------+
|35             |User with webmaster|PASS           |
|               |role can access    |               |
|               |administrative     |               |
|               |features, but user |               |
|               |without webmaster  |               |
|               |role cannot access |               |
|               |administrative     |               |
|               |features           |               |
+---------------+-------------------+---------------+
|36             |New user is        |PASS           |
|               |successfully       |               |
|               |created an the     |               |
|               |password is emailed|               |
|               |to the Case ID     |               |
|               |email address      |               |
+---------------+-------------------+---------------+
|37             |Clicking delete    |PASS           |
|               |next to a user's   |               |
|               |name removes them  |               |
|               |from the list of   |               |
|               |members and any    |               |
|               |attempts to        |               |
|               |manually navigate  |               |
|               |to the user's      |               |
|               |profile fail       |               |
+---------------+-------------------+---------------+
|38             |Editing the user   |PASS           |
|               |and selecting a new|               |
|               |role successfully  |               |
|               |adds that role to  |               |
|               |the user so that on|               |
|               |subsequent page    |               |
|               |loads the new roles|               |
|               |appears.           |               |
+---------------+-------------------+---------------+
|39             |An edit link       |PASS           |
|               |appears on that    |               |
|               |user's profile. The|               |
|               |new information    |               |
|               |entered is         |               |
|               |successfully       |               |
|               |displayed on that  |               |
|               |users page         |               |
+---------------+-------------------+---------------+
|40             |Clicking on the    |PASS           |
|               |view link next to a|               |
|               |members name in the|               |
|               |members list shows |               |
|               |that user's        |               |
|               |profile.           |               |
|               |                   |               |
|               |                   |               |
+---------------+-------------------+---------------+
		 
