Website Architecture
====================

General Web Architecture
------------------------

The basic architecture follows a design pattern for the website.

[h!] |image| [fig:generalWebArchitecture]

Multiple users connect to a webserver running our software and database
via the Internet. Setting up a webserver also requires setting up a
Domain Name System (DNS) server and registering a domain name.

The following subsections detail design decisions for each aspect of
this general architecture.

Webserver - Google App Engine
-----------------------------

As shown in figure [fig:generalWebArchitecture], part of the
architecture is the webserver which will run the actual application.
There are two main options for the webserver: buy a computer and
configure it to be a webserver or use a hosting service. In the vision
and scope document for this project one of the assumptions was that the
website will be hosted for free and that the website will be provided
with a free domain name. This rules out the buy and configure a
webserver option. So it is necessary to select a free hosting service.

There are a multitude of free hosting services on the web, but the
services vary in quality and not all packages come with a free domain
name. The free services are often limited in the amount of bandwidth and
storage they can use. Out of the surveyed hosting services with free
packages Amazon EC2 offered the most amount of free bandwidth and
storage. However, using Amazon EC2 would require setup and configuration
of a webserver and database server. In addition Amazon EC2’s free tier
is only free for the first year. After which the user must pay for all
services.

On the other hand Google App Engine (GAE) has a free tier that does not
expire. The amount of resources provided for free are not as high as
Amazon’s free tier, but the service will remain free for the foreseeable
future.

In addition GAE provides a free hostname by giving the application a
subdomain of the appspot.com domain. This means that a domain name will
not need to be purchased and no DNS server will need to be purchased and
configured. An additional benefit of GAE is that the free domain also
comes with a free Secure Socket Layer (SSL) Certificate. An SSL
certificate will be needed to provide secure login pages and to encrypt
and authenticate sensitive information.

Database - Google’s Bigtable Datastore
--------------------------------------

Another part of the architecture shown in figure
[fig:generalWebArchitecture] is the database. Traditional web
applications use a Structured Query Language (SQL) based database such
as MySQL. However, by choosing GAE as the hosting service the website is
restricted to using Google’s Bigtable Datastore.

The advantage of this constraint is that the website’s data is very
unlikely to be lost due to Google’s large number of resources. In
addition defining the schema for the Bigtable datastore is much easier
than in a traditional SQL database. This is because Bigtable is what is
known as a “NoSQL” database. “NoSQL” essentially means that the database
does not have a traditional SQL schema. This means that instead of using
tables like a traditional SQL database, Bigtable uses one “big table”
that stores what are known as “Entities”. Entities are instances of a
“Model”. Models define the datatypes stored in an Entity as well as the
requirements for each field. Models are defined in the code meaning that
the schema can easily be modified. Additionally the schema is
automatically version controlled because it is defined in the code that
is already under version control. Models are also object oriented
meaning that a base model can be defined and generalized to more
specific models. All of these properties make the Google’s Bigtable more
flexible than a traditional database.

The one big disadvantage of Bigtable is that being a datastore type
database there is no such thing as a JOIN operation. Instead any
JOIN-like operation must be implemented by the developers.

Application Language - Python
-----------------------------

Another constraint imposed by the choice of GAE is the language the
website can be written in. GAE applications can be written in Python,
Java, or any other JVM compatible language.

Out of the possible languages Python will be used. Python is cross
platform meaning that all developers can work on the code regardless of
what their operating environment is. Additionally the Python language
has been supported longer by GAE meaning that the documentation and
support is more mature. This will allow developers to worry less about
unsupported features of the language on the hosting platform and more
about the actual functionality of the code.

Application Framework - Flask
-----------------------------

GAE does not require that a web framework is used. However, if a Python
based web framework is not used then a lot of the development time will
be spent implementing the underlying components of a Python Web Server
Gateway Interface (WSGI) application. Dozens of WSGI server frameworks
have been written, such as Flask and Django. It makes no sense to waste
development time working on code that already exists. For this reason a
Python based web development framework has been chosen.

Of the two mentioned frameworks, Django and Flask, Flask has been chosen
as the framework the website will use. Of the two Flask makes less
design decisions for you. For instance Django assumes that the projects
built on top of it will use Django’s database interface. However, that
interface will not work with GAE’s Bigtable datastore. It is possible to
configure Django to use a different database, but it is difficult. Flask
on the other hand is considered a “microframework”. According to Flask’s
website this means that while Flask gives the projects built on it the
basic code such as the WSGI interface, Flask tries not to make higher
level design decisions. However, everything does not need to be
implemented from scratch with Flask. Flask has many extensions available
on their website for common design problems.

Photo Storage - Photobucket
---------------------------

Something that is not part of the general web architecture depicted in
figure [fig:generalWebArchitecture] are outside web services that this
website would be communicating with. This website will need to
communicate with an outside site to satisfy requirements REQ-32 through
REQ-36 and their respective subrequirements.

Those requirements could be satisfied by storing the photos on the GAE
service. However, the free storage space is limited on GAE. If users
want to upload high resolution photographs the free storage will quickly
run out. To mitigate this problem the website will communicate with one
of the many photo sites on the web. For this design Photobucket has been
chosen.

Photobucket is the photo site currently used by the chapter. However, in
the user survey included in appendix A of the software requirements
document many responses included complaints about how difficult it was
to use. Choosing Photobucket as the outside photo service the website
will have access to the existing photos on Photobucket. Yet using
Photobucket’s API this project can improve on photobucket’s UI to
improve ease of use.

Photobucket’s API does have limits on the amount of operations an
application can perform before being charged. However, the limits are
well beyond the expected traffic for this website.

Photobucket’s API is authenticated using OAuth meaning that a developer
account will need to be created and a key for the website will need to
be generated.

Member Avatars - Gravatar
-------------------------

Another outside service this website will be using is Gravatar. Gravatar
allows users to upload a photo which can be used across multiple
websites as an avatar. To use the avatar a user has on their account the
only thing that is needed is the email address associated with the email
on the user’s Gravatar account.

To use the Gravatar account the website only needs to store the email
associated with the Gravatar account. The website can then use the
algorithm documented on the Gravatar website to generate the URL for the
avatar.

APO Chapter Website Architecture
--------------------------------

Taking into account all of the previous design decisions the
architecture in figure [fig:generalWebArchitecture] becomes the
architecture depicted in figure [fig:finalWebArchitecture].

[h!] |image1| [fig:finalWebArchitecture]

.. |image| image:: img/generalWebArchitecture
.. |image1| image:: img/finalWebArchitecture