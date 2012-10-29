Google App Engine (GAE)
=======================

.. toctree::
   :maxdepth: 1

.. _gae:

Google App Engine's SDK provides a number of basic modules that are used within our source code. The following section describes the important aspects of these modules.

:mod:`db` -- Datastore Classes
------------------------------

.. _gaedb:

.. class:: db.Model

    Basic Model instance that provides the following methods.

    .. method:: put()

       Updates the information in the datastore with the information in the Model instance's attributes

       Will create a new entry in the datastore if it doesn't exist

    .. method:: delete()

       Removes the entity from the datastore that this Model instance is associated with

    .. method:: key()

       Returns the key that this Model instance is associated with. The key is used when making references in the datastore

       .. warning:: If the instance has not yet been saved via the `put` method the key method will raise an exception


.. class:: db.PolyModel

   Same as model, however, this model allows for inheritance. This is useful because a base model can be specified that contains attributes that both classes require. The subclasses can then add their own attributes. But most importantly it allows for polymorphic references. That is another model can specify a reference to the Base class and accept a reference to any subclass.
