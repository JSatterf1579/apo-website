:mod:`Crypto` -- PyCrypto Module
================================

.. _Crypto:

This module contains a number of cryptographic algorithms including hashes and random number generators.  Only the functions, classes and methods used by this application are included on this page. For more information on this module please see the official documentation at 
`https://www.dlitz.net/software/pycrypto/ <https://www.dlitz.net/software/pycrypto/>`_

Classes and Functions Utilized
------------------------------

The documentation for the following functions and classes have been
copied from the official documentation linked above.

.. function:: Crypto.Protocol.KDF.PBKDF2(password, salt, dkLen=16, count=1000, prf=None)

   Used to hash the passwords before they are stored in the
   datastore. Also used to verify a supplied password matches the hash
   in the datastore.

   `https://www.dlitz.net/software/pycrypto/api/current/Crypto.Protocol.KDF-module.html <https://www.dlitz.net/software/pycrypto/api/current/Crypto.Protocol.KDF-module.html>`_

.. class:: Crypto.Random.OSRNG.fallback.PythonOSURandomRNG

   Used to generate the salt for User entities in the datastore

   `https://www.dlitz.net/software/pycrypto/api/current/Crypto.Random.OSRNG.fallback.PythonOSURandomRNG-class.html <https://www.dlitz.net/software/pycrypto/api/current/Crypto.Random.OSRNG.fallback.PythonOSURandomRNG-class.html>`_



   





