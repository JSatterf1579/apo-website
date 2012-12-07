Contributing
============

Who Can Contribute
------------------

Anyone who has an interest in improving the website can
contribute. You do not need coding experience. We can use help with
testing, documentation, and graphical elements. If you would like to
help with something other than coding please contact the current APO
webmaster at webmaster@apo.case.edu.

However, if you wish to code this section will provide a short
introduction explaining the required software, how to setup a basic
development environment, and the coding standards that must be followed.

Required Software
-----------------

This website is built using the Python language. The specific version
of Python the code is targeted for is 2.7. In order to run the
software or do any development you will need to install the python
libraries. You can get the libraries from python.org

You will also require the Google App Engine Python SDK. You can get
the libraries from https://developers.google.com/appengine/downloads

You will also need a number of python packages such as Flask, Jinja 2,
and Werkzeug. If you have the pip tool installed then these can easily
be installed by running the command

``pip install Flask Jinja2``

.. note::
   This command must be run as an admin

Downloading the Website Code
----------------------------

The latest version of the code can be found in our Github repository
located at https://github.com/rhololkeolke/apo-website 

If you do not have Git installed you can download it for free. If you
don't want to install git you can download the source as a zip from
the Github website. If you'd like you can fork the repository so that
you have your own copy on Github.

Setting up the Code Base
------------------------

Once you have downloaded a version of the website code you will need
to run the setup script. Navigate to the src/application directory
then run the generate_keys.py from the command line using the
command

``python generate_keys.py``

This will create a new file in the src/application directory called
secret_keys.py. This file contains the secret data used for that
app. If you want to enable support for Facebook integration you will
need to edit the secret_keys.py file and insert your Facebook app ID
and Facebook app secret into the correct places. The places are marked
in the secret_keys.py

Starting the Local Server
-------------------------

In order to run a local development server you will need to run the
dev_appserver.py script located in the Google App Engine SDK. The
command to start the local server on port 8080 is

``python dev_appserver.py src/ -p 8080 -c``

Once you have run this command you can use your web browser and go to localhost:8080

Optional Tools
--------------

If you are testing any integration with outside services such as
Facebook you will also need to use a tool called
localtunnel. localtunnel can be found at http://progrium.com/localtunnel/
