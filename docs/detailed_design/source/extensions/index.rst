Flask Extensions
==========

Developers have written many extensions to Flask. This project uses a few of those extensions. This section does not attempt to be comprehensive documentation for each of these extensions. However, it does provide the bare minimum about what the extension does and points out specific features that are being utilized. Links to the full documentation for each extension are provided.

Flask-Login
-----------

Flask login provides helper methods for the common task of authenticating users. Full documentation can be found at 
`http://packages.python.org/Flask-Login/ <http://packages.python.org/Flask-Login/>`_

Functions and Classes Utilized
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. function:: login_required(fn)

    This is a :term:`decorator` function. If a view function is decorated with this then the user attempting to access this view will need to be authenticated.

.. class:: current_user()

   This class represents the currently logged in user. It provides methods to check if the user is logged in and if the user has reauthenticated within a certain period.
   

Flask-WTF
---------

