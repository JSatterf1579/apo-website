:mod:`photos` -- Photobucket Interface
======================================

.. module:: photos

This module contains all of the helper methods needed to support photo
galleries. It also includes a number of views, templates, and forms
that are used by the main application to render the user interface for
member related tasks.

   For full information about the Photobucket API see
   `Photobucket API Documentation <http://pic.pbsrc.com/dev_help/WebHelpPublic/PhotobucketPublicHelp_Left.htm#CSHID=PB%20API%20Introduction.htm|StartTopic=Content%2FPB%20API%20Introduction.htm|SkinName=WebHelp>`_

:mod:`photos.photos` - Photos Module
------------------------------------

.. module:: photos.photos

.. class:: PhotoBucket(object)

   This class handles all of the oauth related tasks that are
   necessary to talk to photobucket. It provides a number of methods
   that in turn call the methods on the photobucket server via oauth.

   .. attribute:: consumer_token
   .. attribute:: consumer_key
   .. attribute:: application_token
   .. attribute:: application_key

   .. attribute:: base_url

   .. method:: getAlbumList()

      This method uses the  

:mod:`photos.views` - Photos Related Views
-----------------------------------------

.. module:: photos.views

:mod:`photo.models` - Photo Related Models
------------------------------------------

.. module:: photos.models

:mod:`photo.forms` - Photo Related Forms
----------------------------------------

.. module:: photos.forms

Photo Templates
---------------

.. module:: photos.templates

