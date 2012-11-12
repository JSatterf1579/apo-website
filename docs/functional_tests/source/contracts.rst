Contract Tests
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
.. |11| replace:: 11

These tests deal with the Contracts feature of the website.

                                                           
+---------------------------------------------------------------+
|Functional test requirements for REQ-9: Exec members shall be  |
|able to create new contract types                              |
+---------------+---------------+---------------+---------------+
|ID             |Description    |Test Steps     |Expected       |
|               |               |               |Outcome        |
+===============+===============+===============+===============+
||1|            |Test if a non  |Step 1: Go to  |An error       |
|               |exec member can|log in page and|message saying |
|               |create a new   |log in with    |that the user  |
|               |contract type  |username       |doesn't have   |
|               |               |'zzz111' and   |permission to  |
|               |               |password       |access this    |
|               |               |'password'     |page should be |
|               |               |               |displayed      |
|               |               |Step 2: Go to  |               |
|               |               |the create     |               |
|               |               |contract type  |               |
|               |               |page           |               |
|               |               |               |               |
+---------------+---------------+---------------+---------------+
||2|            |Test if an exec|Step 1: Go to  |A message      |
|               |member can     |the log in page|saying the     |
|               |create a new   |and log in with|contract type  |
|               |contract type  |username       |was            |
|               |Tests          |'admin' and    |successfully   |
|               |requirements   |password       |created should |
|               |9.1-9.3        |'password'     |be displayed   |
|               |               |               |               |
|               |               |Step 2: Go to  |               |
|               |               |the create     |               |
|               |               |contract type  |               |
|               |               |page           |               |
|               |               |               |               |
|               |               |Step 3: Enter a|               |
|               |               |number to the  |               |
|               |               |hours required |               |
|               |               |field          |               |
|               |               |               |               |
|               |               |Step 4: Enter a|               |
|               |               |number to the  |               |
|               |               |dues required  |               |
|               |               |field          |               |
|               |               |               |               |
|               |               |Step 5: Enter a|               |
|               |               |number to the  |               |
|               |               |events required|               |
|               |               |field          |               |
|               |               |               |               |
|               |               |Step 6: Click  |               |
|               |               |the create     |               |
|               |               |contract type  |               |
|               |               |button         |               |
+---------------+---------------+---------------+---------------+

+---------------------------------------------------------------+
|Functional test requirements for REQ-10: Members shall be able |
|to view contract types                                         |
+---------------+---------------+---------------+---------------+
|ID             |Description    |Test Steps     |Expected       |
|               |               |               |Outcome        |
+===============+===============+===============+===============+
||3|            |Test if a non  |Step 1: Go to  |An error       |
|               |member can view|the contracts  |message saying |
|               |contract types |page           |that the user  |
|               |               |               |doesn't have   |
|               |               |               |permission to  |
|               |               |               |access this    |
|               |               |               |page should be |
|               |               |               |displayed      |
+---------------+---------------+---------------+---------------+
||4|            |Test if a      |Step 1: Go to  |The contracts  |
|               |member can view|log in page and|page should be |
|               |contract types |log in with    |displayed with |
|               |Tests          |username       |all relevant   |
|               |requirements   |'zzz111' and   |contract       |
|               |10.1-10.3      |password       |information    |
|               |               |'password'     |               |
|               |               |               |               |
|               |               |Step 2: Go to  |               |
|               |               |the contracts  |               |
|               |               |page           |               |
+---------------+---------------+---------------+---------------+

+---------------------------------------------------------------+
|Funtional test requirements for REQ-11: Exec members shall be  |
|able to edit contract require- ments for each contract type    |
+---------------+---------------+---------------+---------------+
|ID             |Description    |Test Steps     |Expected       |
|               |               |               |Outcome        |
+===============+===============+===============+===============+
||5|            |Test if a non  |Step 1: Go to  |An error       |
|               |exec member can|log in page and|message saying |
|               |update a       |log in with    |that the user  |
|               |contract type  |username       |doesn't have   |
|               |               |'zzz111' and   |permission to  |
|               |               |password       |access this    |
|               |               |'password'     |page should be |
|               |               |               |displayed      |
|               |               |Step 2: Go to  |               |
|               |               |the update     |               |
|               |               |contract type  |               |
|               |               |page           |               |
+---------------+---------------+---------------+---------------+
||6|            |Test if an exec|Step 1: Go to  |A message      |
|               |member can     |the log in page|saying the     |
|               |update a new   |and log in with|contract type  |
|               |contract type  |username       |was            |
|               |Tests          |'admin' and    |successfully   |
|               |requirements   |password       |updated should |
|               |11.1-11.3      |'password'     |be displayed   |
|               |               |               |               |
|               |               |Step 2: Go to  |               |
|               |               |the update     |               |
|               |               |contract type  |               |
|               |               |page           |               |
|               |               |               |               |
|               |               |Step 3: Modify |               |
|               |               |the number to  |               |
|               |               |the hours      |               |
|               |               |required field |               |
|               |               |               |               |
|               |               |Step 4: Modify |               |
|               |               |the number to  |               |
|               |               |the dues       |               |
|               |               |required field |               |
|               |               |               |               |
|               |               |Step 5: Modify |               |
|               |               |the number to  |               |
|               |               |the events     |               |
|               |               |required field |               |
|               |               |               |               |
|               |               |Step 6: Click  |               |
|               |               |the updatee    |               |
|               |               |contract type  |               |
|               |               |button         |               |
|               |               |               |               |
+---------------+---------------+---------------+---------------+

+---------------------------------------------------------------+
|Functional test requirements for REQ-12: Brothers and pledges  |
|shall be able to sign a contract                               |
+---------------+---------------+---------------+---------------+
|ID             |Description    |Test Steps     |Expected       |
|               |               |               |Outcome        |
+===============+===============+===============+===============+
||7|            |Test if a      |Step 1: Go to  |A message      |
|               |member can sign|log in page and|saying that the|
|               |a contract     |log in with    |contract was   |
|               |               |username       |successfully   |
|               |               |'zzz111' and   |signed should  |
|               |               |password       |be displayed   |
|               |               |'password'     |               |
|               |               |               |               |
|               |               |Step 2: Go to  |               |
|               |               |the contracts  |               |
|               |               |page           |               |
|               |               |               |               |
|               |               |Step 3: Select |               |
|               |               |a contract type|               |
|               |               |               |               |
|               |               |Step 4: Click  |               |
|               |               |the sign button|               |
+---------------+---------------+---------------+---------------+

+---------------------------------------------------------------+
|Functional test requirements for REQ-13: Brothers and pledges  |
|shall be able to view their con- tract progress                |
+---------------+---------------+---------------+---------------+
|ID             |Description    |Test Steps     |Expected       |
|               |               |               |Outcome        |
+===============+===============+===============+===============+
||8|            |Test if a      |Step 1: Test   |The contracts  |
|               |member can view|REQ-12 first   |page should    |
|               |their contract |(Sign a        |display current|
|               |progress       |contract)      |progress toward|
|               |               |               |the contract   |
|               |               |Step 2: Go to  |type's         |
|               |               |log in page and|requirements.  |
|               |               |log in with    |               |
|               |               |username       |               |
|               |               |'zzz111' and   |               |
|               |               |password       |               |
|               |               |'password'     |               |
|               |               |               |               |
|               |               |Step 3: Go to  |               |
|               |               |the contracts  |               |
|               |               |page           |               |
+---------------+---------------+---------------+---------------+

+---------------------------------------------------------------+
|Functional test requirements for REQ-14: Exec members shall be |
|able to view everyone's contract progress                      |
+---------------+---------------+---------------+---------------+
|ID             |Description    |Test Steps     |Expected       |
|               |               |               |Outcome        |
+===============+===============+===============+===============+
||9|            |Test if a non  |Step 1: Go to  |There should   |
|               |exec member can|log in page and|not be a view  |
|               |view anyone's  |log in with    |contract       |
|               |contract       |username       |progress button|
|               |progress       |'zzz111' and   |displayed      |
|               |               |password       |               |
|               |               |'password'     |               |
|               |               |               |               |
|               |               |Step 2: Go to  |               |
|               |               |the contracts  |               |
|               |               |page           |               |
+---------------+---------------+---------------+---------------+
||10|           |Test if an exec|Step 1: Go to  |The selected   |
|               |member can view|the log in page|member's       |
|               |anyone's       |and log in with|current        |
|               |contract       |username       |progress toward|
|               |progress       |'admin' and    |their contract |
|               |               |password       |type's         |
|               |               |'password'     |requirements   |
|               |               |               |should be      |
|               |               |Step 2: Go to  |displayed      |
|               |               |the update     |               |
|               |               |contract type  |               |
|               |               |page           |               |
|               |               |               |               |
|               |               |Step 3: Click  |               |
|               |               |on the view    |               |
|               |               |contract       |               |
|               |               |progress button|               |
|               |               |displayed      |               |
|               |               |               |               |
|               |               |Step 4: Select |               |
|               |               |a member to    |               |
|               |               |view their     |               |
|               |               |contract       |               |
|               |               |progress       |               |
+---------------+---------------+---------------+---------------+

+---------------------------------------------------------------+
|Functional test requirements for REQ-15: Exec members shall be |
|able to review incomplete contracts and manually pass them     |
+---------------+---------------+---------------+---------------+
|ID             |Description    |Test Steps     |Expected       |
|               |               |               |Outcome        |
+===============+===============+===============+===============+
||11|           |Test if an exec|Step 1: Go to  |A message      |
|               |member can     |the log in page|saying that the|
|               |manually pass  |and log in with|incomplete     |
|               |an incomplete  |username       |contract has   |
|               |contract       |'admin' and    |been passed    |
|               |               |password       |should be      |
|               |               |'password'     |displayed      |
|               |               |               |               |
|               |               |Step 2: Go to  |               |
|               |               |the update     |               |
|               |               |contract type  |               |
|               |               |page           |               |
|               |               |               |               |
|               |               |Step 3: Click  |               |
|               |               |on the view    |               |
|               |               |contract       |               |
|               |               |progress button|               |
|               |               |displayed      |               |
|               |               |               |               |
|               |               |Step 4: Select |               |
|               |               |a member to    |               |
|               |               |view their     |               |
|               |               |contract       |               |
|               |               |progress       |               |
|               |               |               |               |
|               |               |Step 5: Click  |               |
|               |               |on the pass    |               |
|               |               |incomplete     |               |
|               |               |contract button|               |
+---------------+---------------+---------------+---------------+
