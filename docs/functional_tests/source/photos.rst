Photo Gallery Functional Tests
==============================

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

These tests deal with the photo gallery feature of the website

+-----------------------------------------------------------------+
|Functional Tests for REQ-32: Exec members shall be able to       |
|create new photo albums                                          |
+---------------+----------------+---------------+----------------+
|ID             |Description     |Test Steps     |Exected Outcome |
+===============+================+===============+================+
||1|            |Test if exec    |Step 1: login  |The album should|
|               |members can     |with the       |be created with |
|               |create new      |'admin' account|the entered name|
|               |albums. Also    |and password   |and             |
|               |satisifes all   |'password'     |description. The|
|               |REQ-32          |               |album should    |
|               |sub-requirements|Step 2: Go to  |appear on the   |
|               |                |the photo      |photo albums    |
|               |                |albums page    |page.           |
|               |                |               |                |
|               |                |Step 3: Click  |                |
|               |                |the create new |                |
|               |                |album button   |                |
|               |                |               |                |
|               |                |Step 4: Enter a|                |
|               |                |name and       |                |
|               |                |description    |                |
|               |                |               |                |
|               |                |Step 5: Click  |                |
|               |                |the save button|                |
|               |                |               |                |
|               |                |Step 6: Go back|                |
|               |                |to the photo   |                |
|               |                |albums page    |                |
|               |                |               |                |
|               |                |Step 7: Verify |                |
|               |                |that the album |                |
|               |                |was created    |                |
+---------------+----------------+---------------+----------------+

+-----------------------------------------------------------------------+
|Functional Tests for REQ-33: Exec members shall be able to add         |
|photos to albums                                                       |
+---------------+---------------+-----------------------+---------------+
|ID             |Description    |Test Steps             |Expected       |
|               |               |                       |Outcome        |
+===============+===============+=======================+===============+
||2|            |Test if an     |Step 1: Login          |The selected   |
|               |existing photo |with the               |photo is added |
|               |can be added to|'admin' user           |to the selected|
|               |an existing    |with password          |album. When    |
|               |album          |'password'             |viewing the    |
|               |               |                       |album page of  |
|               |               |Step 2: Go to the view |the selected   |
|               |               |all photos page. If no |album the      |
|               |               |photos are present then|selected photo |
|               |               |complete test |6|      |will be        |
|               |               |before restarting this |displayed.     |
|               |               |test                   |               |
|               |               |                       |               |
|               |               |Step 3: Select         |               |
|               |               |a photo from           |               |
|               |               |the list               |               |
|               |               |                       |               |
|               |               |Step 4: Click          |               |
|               |               |the add photo          |               |
|               |               |to album button        |               |
|               |               |                       |               |
|               |               |Step 5: Select         |               |
|               |               |an existing            |               |
|               |               |album. If no           |               |
|               |               |album exists           |               |
|               |               |then complete          |               |
|               |               |test |1| before        |               |
|               |               |restarting this        |               |
|               |               |test                   |               |
|               |               |                       |               |
|               |               |Step 6: Click          |               |
|               |               |the add button         |               |
|               |               |                       |               |
|               |               |Step 7: Go to          |               |
|               |               |the photo              |               |
|               |               |albums page            |               |
|               |               |                       |               |
|               |               |Step 8: Click          |               |
|               |               |on the album           |               |
|               |               |that the photo         |               |
|               |               |was added to.          |               |
|               |               |                       |               |
|               |               |Step 9: Verify         |               |
|               |               |that the               |               |
|               |               |selected photo         |               |
|               |               |is in the album        |               |
|               |               |that was               |               |
|               |               |selected               |               |
|               |               |                       |               |
|               |               |                       |               |
|               |               |                       |               |
+---------------+---------------+-----------------------+---------------+
||3|            |Test if a photo|Step 1: Login with the |The information|
|               |can be given a |user 'admin' and       |entered in the |
|               |description    |password 'password'    |description    |
|               |               |                       |shoudl match   |
|               |               |Step 2: Go to the view |the information|
|               |               |all photos page. If no |entered during |
|               |               |photos are displayed   |this test.     |
|               |               |complete test |7|      |               |
|               |               |before restarting this |               |
|               |               |test                   |               |
|               |               |                       |               |
|               |               |Step 3: Select a photo |               |
|               |               |from the list          |               |
|               |               |                       |               |
|               |               |Step 4: Add a          |               |
|               |               |description. If there  |               |
|               |               |is already a           |               |
|               |               |description then edit  |               |
|               |               |it.                    |               |
|               |               |                       |               |
|               |               |Step 5: Click the save |               |
|               |               |button                 |               |
|               |               |                       |               |
|               |               |Step 6: Verify that the|               |
|               |               |information displayed  |               |
|               |               |is the same information|               |
|               |               |entered                |               |
+---------------+---------------+-----------------------+---------------+

+---------------------------------------------------------------+
|Functional Tests for REQ-34: Exec members shall be able to     |
|review photo submissions from members                          |
+---------------+---------------+---------------+---------------+
|ID             |Description    |Test Steps     |Expected       |
|               |               |               |Outcome        |
+===============+===============+===============+===============+
||4|            |Test if a photo|Step 1: Login  |The photo will |
|               |can be rejected|with the       |show up under  |
|               |               |user'admin' and|the rejected   |
|               |               |password       |photos section |
|               |               |'password'     |with the       |
|               |               |               |message that   |
|               |               |Step 2: Go to  |was entered    |
|               |               |the review     |during the     |
|               |               |photo          |test.          |
|               |               |submissions    |               |
|               |               |page. If no    |               |
|               |               |photos are     |               |
|               |               |shown complete |               |
|               |               |test |7| before|               |
|               |               |completing this|               |
|               |               |test           |               |
|               |               |               |               |
|               |               |Step 3: Select |               |
|               |               |a photo        |               |
|               |               |               |               |
|               |               |Step 4: Click  |               |
|               |               |the reject     |               |
|               |               |button         |               |
|               |               |               |               |
|               |               |Step 5: Enter a|               |
|               |               |message in the |               |
|               |               |message field  |               |
|               |               |               |               |
|               |               |Step 6: Click  |               |
|               |               |the save button|               |
|               |               |               |               |
|               |               |Step 7: Go back|               |
|               |               |to the review  |               |
|               |               |photo          |               |
|               |               |submissions    |               |
|               |               |page           |               |
|               |               |               |               |
|               |               |Step 8: Verify |               |
|               |               |that the photo |               |
|               |               |now shows up at|               |
|               |               |rejected with  |               |
|               |               |the message    |               |
|               |               |that was       |               |
|               |               |entered.       |               |
+---------------+---------------+---------------+---------------+
||5|            |Test if a photo|Step 1: Login  |The photo that |
|               |can be accepted|with the user  |was accepted   |
|               |               |'admin' and    |should appear  |
|               |               |password       |on the all     |
|               |               |'password'     |photos page    |
|               |               |               |               |
|               |               |Step 2: Go to  |               |
|               |               |the review     |               |
|               |               |photo          |               |
|               |               |submissions    |               |
|               |               |page. If there |               |
|               |               |are no photos  |               |
|               |               |then complete  |               |
|               |               |test |7| before|               |
|               |               |completeing    |               |
|               |               |this test      |               |
|               |               |               |               |
|               |               |Step 3: Select |               |
|               |               |a photo        |               |
|               |               |               |               |
|               |               |Step 4: Click  |               |
|               |               |the accept     |               |
|               |               |button         |               |
|               |               |               |               |
|               |               |Step 5: Go to  |               |
|               |               |the view all   |               |
|               |               |photos page    |               |
|               |               |               |               |
|               |               |Step 6: Verify |               |
|               |               |that the photo |               |
|               |               |is on the all  |               |
|               |               |photos page    |               |
|               |               |               |               |
+---------------+---------------+---------------+---------------+

+----------------------------------------------------------------+
|Functional Tests REQ-35: Members shall be able to view existing |
|albums and photos                                               |
+---------------+----------------+---------------+---------------+
|ID             |Description     |Test Steps     |Expected       |
|               |                |               |Outcome        |
+===============+================+===============+===============+
||6|            |Test if members |Step 1: Login  |The album and  |
|               |can view albums |with the user  |its description|
|               |and individual  |'test' and     |should be      |
|               |photos. Also    |password       |displayed. The |
|               |tests all       |'password'     |photo that is  |
|               |sub-requirements|               |selected should|
|               |of REQ-35       |Step 2: Go to  |be displayed   |
|               |                |the photo      |along with its |
|               |                |albums page.   |description    |
|               |                |               |               |
|               |                |Step 3: Select |               |
|               |                |an album.      |               |
|               |                |               |               |
|               |                |Step 4: Verify |               |
|               |                |that the album |               |
|               |                |is displayed   |               |
|               |                |along with the |               |
|               |                |album          |               |
|               |                |description.   |               |
|               |                |               |               |
|               |                |Step 5: Select |               |
|               |                |a photo in the |               |
|               |                |album          |               |
|               |                |               |               |
|               |                |Step 6: Verify |               |
|               |                |that the photo |               |
|               |                |and description|               |
|               |                |is displayed.  |               |
+---------------+----------------+---------------+---------------+

+---------------------------------------------------------------+
|Functional Tests REQ-36: Members shall be able to submit photos|
|to albums for review                                           |
+---------------+---------------+---------------+---------------+
|ID             |Description    |Test Steps     |Expected       |
|               |               |               |Outcome        |
+===============+===============+===============+===============+
||7|            |Test if members|Step 1: Login  |The photo that |
|               |can submit a   |with the user  |ws submitted   |
|               |photo with a   |'test' and     |should appear  |
|               |description    |password       |in the         |
|               |               |'password'     |unreviewed list|
|               |               |               |with the       |
|               |               |Step 2: Go to  |description    |
|               |               |the submit a   |that was       |
|               |               |photo page     |entered.       |
|               |               |               |               |
|               |               |Step 3: Click  |               |
|               |               |the browse     |               |
|               |               |button. Select |               |
|               |               |a photo on the |               |
|               |               |computer.      |               |
|               |               |               |               |
|               |               |Step 4: Add a  |               |
|               |               |description    |               |
|               |               |               |               |
|               |               |Step 5: Click  |               |
|               |               |the submit     |               |
|               |               |button         |               |
|               |               |               |               |
|               |               |Step 6: Login  |               |
|               |               |with the user  |               |
|               |               |'admin' user   |               |
|               |               |with password  |               |
|               |               |'password'     |               |
|               |               |               |               |
|               |               |Step 7: Go to  |               |
|               |               |the review     |               |
|               |               |photos page    |               |
|               |               |               |               |
|               |               |Step 8: Verify |               |
|               |               |that the photo |               |
|               |               |is in the      |               |
|               |               |unreviewed     |               |
|               |               |section with   |               |
|               |               |the description|               |
|               |               |entered.       |               |
+---------------+---------------+---------------+---------------+



