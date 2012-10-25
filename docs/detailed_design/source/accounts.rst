:mod:`application.accounts` -- User Account Module
==================================================

.. automodule:: application.accounts
   :members:

.. autofunction:: application.accounts.load_user(userid)

   This functions is required by Flask-Login.

   It uses the login manager's user_loader decorator.

   The purpose of this function is to return the User entity with the matching userid.

   :param userid: The unique user identifier. Currently this is a unicode version of the cwru ID
   :type userid: unicode

   :rtype: application.models.User




