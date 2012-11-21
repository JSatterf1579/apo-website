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

   This class is a Proxy for the Photobucket methods

   .. attribute:: consumer_token
   .. attribute:: consumer_key
   .. attribute:: application_token
   .. attribute:: application_key

   .. attribute:: base_url

  .. attribute:: __request
  
     * Type of Oauth.Request -- this is used by all the methods to perform the oauth operations

   .. method:: __init__(consumer_token, consumer_key, application_token, application_key)

      This method sets all of the attributes so that the 

   .. method:: get_albumList()

      This method uses the photobucket `Get User URL's method <http://pic.pbsrc.com/dev_help/WebHelpPublic/Content/Methods/User/Get%20User%20URL.htm>`_

      It takes the information recevied from that method and parses
      out the album urls. It returns a list of the parse album urls

   .. method:: get_album(albumName)

      This method uses the photobucket `Get Album Method <http://pic.pbsrc.com/dev_help/WebHelpPublic/Content/Methods/Album/Get%20Album.htm>`_

      It takes in an album name and retrieves a list of all photos in
      the album along with the associated album information. It parses
      out the photo information and puts it in an instance of the
      :class:`PhotoBucket.Image` internal class. It returns of a list
      of these Image objects.

   .. method:: upload_photo_to_album(album, photo[, title=""[, desc=""]])

      This method uses the photobucket `Upload Media to Album Method <http://pic.pbsrc.com/dev_help/WebHelpPublic/Content/Methods/Album/Upload%20Media%20to%20an%20Album.htm>`_

      It takes an album name and photo file and optionally a title and
      description. It then uploads it to the server. Returns True if
      successful, False otherwise.

      :param album: Name of album of album
      :type album: unicode
      
      :param photo: Photo File
      
      :param title: Title of photo
      :type title: unicode
      
      :param desc: Description of photo
      :type desc: unicode

      :rtype: bool - True if successful, False otherwise

   .. method:: delete_photo(photoUrl)
   
      This method uses the photobucket `Delete Media method <http://pic.pbsrc.com/dev_help/WebHelpPublic/Content/Methods/Media/Delete%20Media.htm>`_

      It takes a photo URL and deletes the object on the photobucket
      server. Returns True if successful, False otherwise

      :param photoUrl: Photo URL
      :type photoUrl: unicode

      :rtype: bool - True if successful, False otherwise

   .. class:: PhotoBucket.Image(object)
   
      This class holds all of the information about an image in
      photobucket.

      .. attribute:: url - url of the image

      .. attribute:: thumb - url of thumbnail

      .. attribute:: description - photo description

      .. attribute:: title - title of photo

   

:mod:`photos.views` - Photos Related Views
-----------------------------------------

.. module:: photos.views

.. function:: viewAlbumList()

   This function retrieves a list of albums from photobucket using an
   instance of the PhotoBucket class.

   It accepts GET requests

   Upon receiving a GET request it retrieves the list of photos from
   photobucket. It renders the :ref:`View Album List Template` to
   display the list

.. function:: viewAlbum(albumName)

   This function takes in an album name as part of the url.  It then
   retrieves the album and all of its images via an instance of the
   PhotoBucket class

   It accepts GET requests.
   
   Upon receiving a GET request it retrieves all of the images and
   then renders the thumbnails via the :ref:`View Album Template`.

.. function:: viewPhoto(albumName, photoName)

   This function takes in an album name and a photo name from the url. It then
   retrieves the specific photo and all of its metadata.

   It accepts GET requests

   Upon receiving a GET request it retrieves the specified image and
   then displays the photo and its metadata via the :ref:`View Photo Template`

.. function:: deletePhoto(photoName)

   This function takes a photo name from the url and then attempts to
   delete the photo on the Photobucket site.

   It accepts GET requests

   Upon receiving the GET request it sends a delete request to the
   PhotoBucket server. If the request is successful it forwards the
   user back to the viewAlbumList function. If it isn't successful an
   error message is displayed.

   This requires the user to be logged in

.. function:: uploadPhoto(albumName)

   This function takes a photofile and uploads it to the album name
   specified in the URL.

   It accepts a GET and POST request

   Upon receiving the POST request it sends the photo to the server
   and if the result is successful the user is forwarded to the
   viewAlbum function for the specified album. Otherwise an error
   message is displayed.

   If a GET request is received the :ref:`Upload Photo Template` is
  rendered with the :class:`photo.forms.UploadPhotoForm`

   This requires the user to be logged in



:mod:`photo.models` - Photo Related Models
------------------------------------------

.. module:: photos.models

Everything is loaded on the fly from the photobucket server so there
are no models required.

:mod:`photo.forms` - Photo Related Forms
----------------------------------------

.. module:: photo.forms

.. class:: photo.forms.UploadPhotoForm

   .. attribute:: file
   
      * FileField
      * Required

   .. attribute:: title
   
      * TextField
      * Optional

   .. attribute:: description
   
      * TextField
      * Optional

Photo Templates
---------------

.. module:: photos.templates


View Album List Template
************************

This template displays a list of albums. It requires a list of urls
for the albums it needs to display.


View Album Template
*******************

This template displays a single album and thumbnails of all of its
images. It requires :class:`photos.photos.PhotoBucket.Image` instances
for each image in the album that is to be displayed.

View Photo Template
*******************

This template displays a single photo and its associated meta data. It
requires a :class:`photos.photos.PhotoBucket.Image` instance for the photo.

Upload Photo Template
*********************

This template displays an Upload Photo Form. It requires and instance
of :class:`photo.form.UploadPhotoForm`


