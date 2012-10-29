Introduction
============

Document Overview
-----------------

The is a new website designed to replace the existing website. The
current website provides basic administrative features for some of the
executive positions. It also provides some basic features that allow
brothers to keep in touch. However, each semester more features are
requested and the current website was not designed with future
maintainability in mind. For this reason this project seeks to make a
new website that will provide better administrative tools and better
social tools. The goal is for the website to decrease the amount of
effort needed for administration and to get chapter members more
involved in the organization. This document lays out the design for the
new website including the overall architecture, rationale for selected
components and services, and the specifications of new components and
services which must be created.

Document Conventions
--------------------

This document references previous documents created for this project as
well as documentation for outside systems this system will interact
with. References for the system can be found throughout the document.

Specification Syntax
**************************

Class definitions begin with the word *class* followed by the class
name namespaced by the package and modules it is contained in. After
the class name is a set of parenthesis. Superclasses of that class are
listed inside of these parenthesis. This is the syntax used to define
inheritance in python

Methods are listed under a class and are indented. They are shown in
bold with parenthesis. Inside the parenthesis are the names of the
arguments. If an argument name is followed by an equals sign and
something else then that argument defaults to the value after the
equals and the method can be called without supplying that
argument. Optional arguments are shown inside of square brackets.

Please note that there are two special types of arguments in python
\*args and \*\*kwargs. Args is a variable length list of argument
values. kwargs is a dictionary of keys and values. The key value pairs
are passed into a function in the form `name=value`.

Functions are specified the same as methods. However, they are not
indented under a class

Class attributes are listed under a class, but they do not contain
parenthesis. If the attribute has special properties they are listed
as bullets under that attribute.

For example

.. class:: Example.Eg(object)

   This is a class definition of a class called Eg inside of the
   Example module. It inherits from the Python provided object class.

   .. attribute:: attribute1

      * This is a special property of attribute1

   .. method:: listExamples(required[, optional=None[, *args[,  **kwargs]]])

      This is a method on the class Eg. It has a required parameter
      called required. It has an optional parameter that defaults to
      type None. It also allows a variable list of arguments and a
      variable list of `name=value` pairs.

      For example

           Eg.listExamples("required")

      or

           Eg.listExamples("required", optional="optional", "arg1", "arg2", kwarg1="kwarg1", kwarg2="kwarg2")



