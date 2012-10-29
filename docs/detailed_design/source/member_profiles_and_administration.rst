:mod:`members` -- Member Profiles and Member Administration
=========================================

.. module:: members

This module contains contains all of the helper methods needed to
support member profiles and member administration. It also include a
number of views, templates and forms that are used by the main
application to render the user interface for member related tasks.

:mod:`members.members` -- Members Module
----------------------------------------

.. module:: members.models

.. function:: get_avatar_url(avatar_address)

   This function takes the avatar field and converts it to a gravatar
   image url.

   :param avatar_address: The avatar field from the :class:`accounts.models.__UserModel`
   :type avatar_address: unicode

   :rtype: unicode url for avatar image

:mod:`members.models` -- Member Related Models
----------------------------------------------

.. module:: members.models

.. class:: accounts.models.AddressModel(db.Model)

   Contains an address for a User

   .. method:: __init__(user, address[, name])

       Creates a new Address entity

       :param user: User this address belongs to
       :type user: application.models.User

       :param address: Address
       :type address: google.appengine.ext.db.PostalAddress 

       :param name: Nickname for Address - e.g. home
       :type name: unicode

.. class:: accounts.models.PhoneNumberModel(db.Model)

   Contains a phone number for a User

   .. method:: __init__(user, number[, name])

       Creates a new PhoneNumber entity

       :param user: User this phone number belongs to
       :type user: application.model.User

       :param number: Phone number with in the following format "(111) 555-3333"
       :type number: google.appengine.ext.db.PhoneNumber

       :param name: Optional nickname for phone number - e.g. cell
       :type name: unicode

.. class:: accounts.models.EmailAddressModel(db.Model)

   Contains an email address for a User

   .. method:: __init__(user, email[, name])

       Creates a new Email entity

       :param user: User this email address belongs to
       :type user: application.model.User

       :param email: User's email
       :type email: google.appengine.ext.db.Email

       :param name: Optional nickname for address - e.g. school
       :type name: unicode

:mod:`members.views` -- Member Related Views
--------------------------------------------

.. module:: members.views

.. function:: createUser()

   This method is used for creating new users. It is responsible for
   collecting the information necessary to use the
   :func:`members.members.createUser` function.

   It accepts a GET and POST request.

   If a POST request expects the information from
   :class:`members.forms.CreateMemberForm` to be present

   If a GET request the :ref:`Create Member Template` will be
   rendered.

   Requires that the user be logged in and have a role of Administrator

.. function:: listUsers()

   This method is used to list all of the current members. Retrieves a
   list of all users. It filters that list if search parameters are present.

   It accepts a GET and POST request.

   If a POST request expects information from
   :class:`members.forms.UpdateSearchMembersForm` to be present. It will
   then render the :ref:`List Members Template` with only the members
   matching the search criteria.

   If a GET request displays the :ref:`List Members Template`

   This method requires that the user be logged in.
   
   If the user has the role of an Administrator then links to edit and
   delete each user will also be displayed.

.. function:: deleteUser(cwruID)

   This method takes a cwruID from the url and deletes the user with
   that id.

   It accepts a GET request

   If the deletion is successful the user is redirected back to the
   listUsers view. If deletion is unsuccessful the user is shown an
   error message.

   This method requires that the user be logged in and have a role of Administrator.

.. function:: viewUser(cwruID)

   This method takes a cwruID from the url and retrieves the user
   account and profile information associated with that account. It
   then displays the profile using the :ref:`View Profile Template`.

   It accepts a GET request

   This method requires that the user is logged in. If the user logged
   in has the same cwruID as the profile requested a link to edit the
   profile is also displayed on the page.

   If the user has an Administrator role then the link to edit is displayed.

.. function:: editUser(cwruID)

   This method takes a cwruID from the url and retrieves the user
   account and profile information associated with that account.

   It accepts a GET and POST request.

   If it is a POST request the view looks for data from zero or more
   :class:`members.forms.AddressForm` form, zero or more
   :class:`members.forms.PhoneNumberForm`, zero or more
   :class:`members.forms.EmailAddressForm`, and one
   :class:`members.forms.UpdateUserForm`.

   It uses the information received in the POST request to update the
   user instance in the database. It then redirects the user to the
   viewUser view to display the changes.

   If it is a GET request a :class:`members.forms.AddressForm` for each
   :class:`members.models.AddressModel` in the datastore for that user
   is displayed. Additionally a :class:`members.forms.PhoneNumberForm`
   for each
   :class:`members.models.PhoneNumberModel` in the datastore for that
   user is displayed. Also a :class:`members.forms.PhoneNumberForm`
   for each
   :class:`members.models.EmailNumberModel` associated with the user
   is displayed. These forms are populated with the information in
   each of the models. Additionally a blank one of each form is provided in
   case the user wants to add an additional phone number, address, or
   email. Finally a :class:`members.models.UpdateSearchUserForm` is
   displayed. When the user saves the changes they are POSTed to this
   view. All of this is rendered in the :ref:`Edit User Template`.

   This view requires that the logged in user be the same user that is
   being edited.
   
   However, if the user has an Administrator role that user can also
   access this page. 

   

:mod:`members.forms` -- Member Related Forms
--------------------------------------------

.. module:: members.forms

.. class:: members.forms.AddressForm

   This class is used for validating an address

   .. attribute:: addrName - Specifies a nickname for the address

      * TextField

   .. attribute:: street1 - first line of an address

      * TextField
      * Required

   .. attribute:: street2 - second line of an address

      * TextField
      * Required

   .. attribute:: city

      * TextField
      * Required

   .. attribute:: state

      * TextField
      * Required

   .. attribute:: zip

      * TextField
      * Required

.. class:: members.forms.PhoneNumberForm

   This class is used for validating a phone number

   .. attribute:: phoneNumber

      * PhoneField
      * Required

.. class:: members.forms.EmailAddressForm

   This class is used for validating an email address

   .. attribute:: emailAddress
   
      * EmailField
      * Required

.. class:: members.forms.UpdateSearchUserForm

   This class is used for collecting information to update a user
   profile.

   .. attribute:: firstName
      
      * TextField
      * Required

   .. attribute:: middleName

      * TextField
      * Optional

   .. attribute:: lastName

      * TextField
      * Required

   .. attribute:: family
      
      * TextField
      * Optional

   .. attribute:: big
      
      * TextField
      * Optional

   .. attribute:: avatar

      * EmailField
      * Optional

   .. attribute:: roles

      * TextField
      * Optional

.. class:: members.forms.CreateUserForm

   This class is used for collecting information to create a user
   profile.

   .. attribute:: firstName
      
      * TextField
      * Required

   .. attribute:: middleName

      * TextField
      * Optional

   .. attribute:: lastName

      * TextField
      * Required

   .. attribute:: cwruID

      * TextField
      * Required

   .. attribute:: family
      
      * TextField
      * Optional

   .. attribute:: big
      
      * TextField
      * Optional

   .. attribute:: avatar

      * EmailField
      * Optional

    .. attribute:: roles
      
      * TextField
      * Optional


Member Templates
----------------

.. module:: accounts.templates

Create Member Template
**********************

This template renders the form to create members.

It requires an instance of the :class:`members.forms.CreateMemberForm`.

List Members Template
*********************

This templates displays a list of all users matching the information
from the search form.

It also renders the search form.

It requires an instance of the
:class:`members.forms.UpdateSearchMemberForm`. It also requires
instances of the :class:`accounts.accounts.__User` model for all users
to be displayed.

View Profile Template
*********************

This template displays a member profile.

It requires an instance of the user to be displayed and instances of
the member profile models such as :class:`members.models.AddressModel`

Edit User Template
******************

This template renders the forms to update a user

It requires an instance of the user to be displayed and instances of
the member profile models such as :class:`members.models.AddressModel`



