:mod:`application.contract` -- Contract Tracking Package
========================================================
Classes
*******


:mod:`contract.contract` -- Contract class
------------------------------------------

.. module:: contract.contract

.. class:: contract(object)
    
   The contract class will allow :term:`brother`s to create and sign :term:`contract`s.
   The contract class will also allow tracking of contract requirements.
   It contains the information about specific service events in the datastore.
   
   .. method:: save()
   Saves the attributes attached to the class instance to the Contract datastore object   
  
   .. method:: delete()
   Removes the current class instance Contract object from the datastore
   
   .. method:: __setattr__(self, name, value)

   This method overides the built in __setattr__ method. This
   method allows setting of the internal database model's
   parameters by the normal "Object.attr = value" syntax.
   
   This method disallows adding any field that is not in the
   Contract class. All values will be saved as
   an attribute on this instance.

   If an attribute is required in the datastore instance it is
   required here. Meaning it cannot be set to None or blank.

   A validator is code that checks for certain properties of an attribute.

   It contains special validators for the following fields
   
   hourReq.hours - must be greater than or equal to 0
   
   duesReq.amount - must be greater than or equal to 0
   
   attendanceReq.amount - must be greater than or equal to 0
      
Module Functions
****************

.. function:: contract.contract.createContract

   This method is a factory method for service contracts. 

.. function:: contract.contract.contractList

   This method returns a list of current contract types from the datastore.

.. function:: contract.contract.signContract

   This method assigns a contract type to a User (Can be null).
   
.. function:: contract.contract.verifyContract

   This method compares a User's contract requirements and contract type requirements and 
   determines if the requirements are satisfied.

:mod:`contract.models` -- Contract related Models
-------------------------------------------------

.. module:: contract.models

.. method:: ChapterEvent()

   Creates a new ChapterEvent entity
   
   :param date: Date of event
   :type date: datetime.date
   

.. method:: Contract(name)

   Creates a new Contract entity

   :param name: Name of contract - e.g. associate
   :type name: unicode

.. method:: Requirement(contract, dueDate[, name])

   Creates a new Requirement entity

   :param contract: Contract this requirement is associated with
   :type contract: application.models.Contract

   :param dueDate: Date this requirement is due
   :type dueDate: datetime.date

   :param name: Optional nickname for requirement - e.g. inside hours
   :type name: unicode

.. method:: HourReq(min, type)

   Creates a new HourReq entity

   :param min: Minutes needed to meet this requirement
   :type min: int

   :param type: Type of minutes needed - e.g. inside
   :type type: unicode

.. method:: DuesReq(amount)

   Creates a new DuesReq entity

   :param amount: Amount of money need to meet this requirement
   :type amount: float

.. method:: AttendanceReq(amount, type)

   Creates a new AttendanceReq entity

   :param amount: Amount of events needed to meet this requirement. Allows for fractions of events to be specified
   :type amount: float

   :param type: Type of event needed - e.g. ServiceEvent
   :type type: unicode   
    
:mod:`contract.views` -- Contract related views
-----------------------------------------------

.. module:: contract.views

.. class:: CreateContractView()

The CreateContractView is used to provide the view for creating contracts.
   This view requires a current :term:`exec` User instance
   This view responds to get and post requests
  :post: causes the view to store the submitted create contract information to the datastore
  :get: displays the list of existing contract types.
This view uses a template
  :Template: application.contract.CreateContractTemplate()
  
.. class:: SignTrackContractView()

The signTrackContractView is used to sign and track contract hours.
    This view requires a current User instance
    This view responds to get and post requests
   :post: causes the view to store the contract signed type and information to the datastore
   :get: displays a list of the contract types available or displays a list of requirements and the progress made toward them
This view uses a template
   :Template: application.contract.SignTrackContractTemplate() 
   
:mod:`contract.forms` -- contract related forms
--------------------------------------------------------
   
.. module:: contract.forms   

.. class:: CreateContractForm(Form)

This form contains the fields for filling out the parameters of a contract in conjunction with
contract.contract.createContract

   .. method:: CreateUpdateContractForm(name, hours, minutes, hoursDueDate, amount, duesDueDate, attendanceReq, attDueDate)
        
   :param name: Name of contract
   :type name: unicode       
   :param hours: Hours needed to fulfill contract
   :type hours: int
   :param minutes: Minutes needed to fulfill contract
   :type minutes: int
   :param hoursDueDate: Date that all hours and minutes must be completed
   :type hoursDueDate: datetime.date
   :param amount: Dues owed
   :type amount: int
   :param duesDueDate: Date that dues must be paid by
   :type duesDueDate: datetime.date
   :param attendanceReq: Number of chapter meetings that must be attended
   :type attendanceReq: int
   :param attDueDate: Date that the required number of attended meetings must be met by
   :type attDueDate: datetime.date
       
   :rtype: Form instance
   
:mod:`contract.templates` -- contract related templates
----------------------------------------------------------------

.. module:: contract.templates

.. class:: CreateContractTemplate()

Used to display create contract form. 

   :Requires: application.serviceEvent.CreateUpdateContractForm()
Extends  
   :extends: MainTemplate
   :extends: CreateContractView()
   
.. class:: SignTrackContractTemplate()

Used to sign and track contracts. 

Extends  
   :extends: MainTemplate
   :extends: SignTrackContractView()