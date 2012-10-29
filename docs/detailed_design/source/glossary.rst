Glossary
========

.. glossary::

   decorator
     A special type of function in python that takes in a function
     reference and optionally other parameters. This function wraps
     the function with additional code that should be run whenever the
     function is executed. 

     Decorators go directly above the function name and are proceded
     by an `@` symbol. The first parameter is always the function
     reference and when using the `@` syntax this parameter doesn't
     need to be explicitly stated. The next function the interpreter
     encounters will be used.

     .. code-block:: python

        def my_decorator(fn, optional_argument):
	    # do something to the function here
	    pass
     
        @my_decorator(optional_argument)
	my_decorated_function(*args, **kwargs):
	    # code goes here
	    pass

   Google App Engine
      Hosting provided by Google for web applications developed using
      Python, Java and Go.

   GAE
      :term:`Google App Engine`

   Password Based Key Derivation Function 2
      A secure password hashing algorithm. Not only does it prevent
      reversal of the hash to the original password, it also provides
      intentional delays to prevent brute force attacks.



   PBKDF2
      :term:`Password Based Key Derivation Function 2`

