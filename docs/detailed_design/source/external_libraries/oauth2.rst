python-oauth2 -- A library for communicating with Oauth providers
================================================================

In order to communicate with Photobucket and other Oauth providers the application must implement the Oauth protocol. This protocol is widely used meaning there are a number of libraries that already implement the protocol. The official Oauth website recommends the "python-oauth2" library written by github user "simplegeo". The repository containing all of the source code and the full documentation can be found at `https://github.com/simplegeo/python-oauth2 <https://github.com/simplegeo/python-oauth2>`_

Oauth Protocol Overview
-----------------------

Oauth allows third party websites to access services on behalf of a user without the user actually giving the third party their login credentials. Each application is a given an application key by the oauth provider. This means if an application abuses the oauth provider's service the application can be revoked rights.  Additionally each user that has allowed the third party access gets a unique consumer token. This token can be revoked by the user at anytime. If revoked the third party can no longer access the client's resources on the oauth provider's server.

The full oauth description including all of the details about how the protocol works can be found at `Oauth.net <http://oauth.net/>`_

Library Functions Utilized
--------------------------

.. function:: oauth.Request(method, url, parameters)

   This function takes a request type (GET or POST), a url, and a dictionary of parameters. It then creates a request object. This object can be used to sign a request and to get the request URL.

.. function:: oauth.SignatureMethod_HMAC_SHA1()

   This function is used to sign a request object with the SHA1 hash.

.. function:: Request.to_url()

    This function returns the url for the Request instance. It is responsible for 



