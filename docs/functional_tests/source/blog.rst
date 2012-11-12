Blog Tests
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

These tests deal with the Blogs feature of the website.

+---------------------------------------------------------------+
|Functional test requirements for REQ-27: Exec members shall be |
|able to write new blog posts                                   |
+---------------+---------------+---------------+---------------+
|ID             |Description    |Test Steps     |Expected       |
|               |               |               |Outcome        |
+===============+===============+===============+===============+
||1|            |Test if a non  |Step 1: Go to  |An error       |
|               |exec member can|log in page and|message saying |
|               |create a new   |log in with    |that the user  |
|               |blog post      |username       |doesn't have   |
|               |               |'zzz111' and   |permission to  |
|               |               |password       |access this    |
|               |               |'password'     |page should be |
|               |               |               |displayed      |
|               |               |Step 2: Go to  |               |
|               |               |the create new |               |
|               |               |blog post page |               |
|               |               |               |               |
+---------------+---------------+---------------+---------------+
||2|            |Test if an exec|Step 1: Go to  |A message      |
|               |member can     |the log in page|saying the blog|
|               |create a new   |and log in with|post was       |
|               |contract type  |username       |successfully   |
|               |               |'admin' and    |created should |
|               |               |password       |be displayed   |
|               |               |'password'     |               |
|               |               |               |               |
|               |               |Step 2: Go to  |               |
|               |               |the create new |               |
|               |               |blog post page |               |
|               |               |               |               |
|               |               |Step 3: Enter a|               |
|               |               |title to the   |               |
|               |               |title field    |               |
|               |               |               |               |
|               |               |Step 4: Enter  |               |
|               |               |any text to the|               |
|               |               |entry field    |               |
|               |               |               |               |
|               |               |Step 5: Click  |               |
|               |               |the create blog|               |
|               |               |post button    |               |
|               |               |               |               |
+---------------+---------------+---------------+---------------+

+---------------------------------------------------------------+
|Functional test requirements for REQ-28: Exec members shall be |
|able to edit existing blog posts                               |
+---------------+---------------+---------------+---------------+
|ID             |Description    |Test Steps     |Expected       |
|               |               |               |Outcome        |
+===============+===============+===============+===============+
||3|            |Test if a non  |Step 1: Go to  |An edit blog   |
|               |exec member can|log in page and|post button    |
|               |edit a blog    |log in with    |should not be  |
|               |post           |username       |displayed      |
|               |               |'zzz111' and   |               |
|               |               |password       |               |
|               |               |'password'     |               |
|               |               |               |               |
|               |               |Step 2: Go to  |               |
|               |               |the blog page  |               |
|               |               |               |               |
+---------------+---------------+---------------+---------------+
||4|            |Test if an exec|Step 1: Go to  |A message      |
|               |member can     |the log in page|saying the blog|
|               |create a new   |and log in with|post was       |
|               |contract type  |username       |successfully   |
|               |               |'admin' and    |edited should  |
|               |               |password       |be displayed   |
|               |               |'password'     |               |
|               |               |               |               |
|               |               |Step 2: Go to  |               |
|               |               |blog page      |               |
|               |               |               |               |
|               |               |Step 3: Click  |               |
|               |               |the edit blog  |               |
|               |               |post button    |               |
|               |               |               |               |
|               |               |Step 4: Modify |               |
|               |               |the title in   |               |
|               |               |the title field|               |
|               |               |               |               |
|               |               |Step 5: Modify |               |
|               |               |any text in the|               |
|               |               |entry field    |               |
|               |               |               |               |
|               |               |Step 6: Click  |               |
|               |               |the update blog|               |
|               |               |post button    |               |
|               |               |               |               |
+---------------+---------------+---------------+---------------+

+---------------------------------------------------------------+
|Functional test requirements for REQ-29: Exec members shall be |
|able to moderate comments                                      |
+---------------+---------------+---------------+---------------+
|ID             |Description    |Test Steps     |Expected       |
|               |               |               |Outcome        |
+===============+===============+===============+===============+
||5|            |Test if a non  |Step 1: Go to  |A remove       |
|               |exec member can|log in page and|comment button |
|               |remove a blog  |log in with    |should not be  |
|               |comment        |username       |displayed next |
|               |               |'zzz111' and   |to any comments|
|               |               |password       |other than     |
|               |               |'password'     |those made by  |
|               |               |               |the member     |
|               |               |Step 2: Go to  |               |
|               |               |the blog page  |               |
+---------------+---------------+---------------+---------------+
||6|            |Test if an exec|Step 1: Go to  |A message      |
|               |member can     |the log in page|saying the     |
|               |remove a blog  |and log in with|comment was    |
|               |comment        |username       |successfully   |
|               |               |'admin' and    |removed should |
|               |               |password       |be displayed   |
|               |               |'password'     |               |
|               |               |               |               |
|               |               |Step 2: Go to  |               |
|               |               |the blog page  |               |
|               |               |               |               |
|               |               |Step 3: Click  |               |
|               |               |the remove     |               |
|               |               |comment button |               |
|               |               |on any comment |               |
|               |               |               |               |
+---------------+---------------+---------------+---------------+

+---------------------------------------------------------------+
|Functional test requirements for REQ-30: Members and nonmembers|
|will be able to view blog posts                                |
+---------------+---------------+---------------+---------------+
|ID             |Descrption     |Test Steps     |Expected       |
|               |               |               |Outcome        |
+===============+===============+===============+===============+
||7|            |Test if anyone |Step 1: If     |The blog posts |
|               |can view blog  |logged in, log |and associated |
|               |posts          |out            |comments should|
|               |               |               |be displayed   |
|               |               |Step 2: Go to  |               |
|               |               |the blog page  |               |
|               |               |               |               |
+---------------+---------------+---------------+---------------+

+---------------------------------------------------------------+
|Functional test requirements for REQ-31: Members shall be able |
|to comment on blog posts                                       |
+---------------+---------------+---------------+---------------+
|ID             |Description    |Test Steps     |Expected       |
|               |               |               |Outcome        |
+===============+===============+===============+===============+
||8|            |Test if        |Step 1: If     |A comment      |
|               |nonmembers can |logged in, log |button should  |
|               |comment on blog|out            |not be         |
|               |posts          |               |displayed      |
|               |               |Step 2: Go to  |               |
|               |               |the blog page  |               |
|               |               |               |               |
+---------------+---------------+---------------+---------------+
||9|            |Test if members|Step 1: Go to  |A message      |
|               |can comment on |log in page and|saying the     |
|               |blog posts     |log in with    |comment has    |
|               |               |username       |been posted    |
|               |               |'zzz111' and   |should be      |
|               |               |password       |displayed      |
|               |               |'password'     |               |
|               |               |               |               |
|               |               |Step 2: Go to  |               |
|               |               |the blog page  |               |
|               |               |               |               |
|               |               |Step 3: Click  |               |
|               |               |on the comment |               |
|               |               |button         |               |
|               |               |               |               |
|               |               |Step 4: Enter a|               |
|               |               |comment in the |               |
|               |               |comment field  |               |
|               |               |               |               |
|               |               |Step 5: Click  |               |
|               |               |the accept     |               |
|               |               |button         |               |
|               |               |               |               |
+---------------+---------------+---------------+---------------+
