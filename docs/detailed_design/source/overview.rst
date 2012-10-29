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
with. References for the system can be found at the end of the document.
In text citations are listed as numbers in square brackets. For example
“[ 1 ]”.

Definitions and Acronyms
------------------------

p.20p.80

 & A person who was previously a member, but has since graduated
 & A member in the chapter who has guided another member during their
pledging process
 & A general member of the chapter that has gone through the pledging
process.
 & The requirements that a member must satisfy to remain in good
standing with the chapter
 & A general member of the chapter (brother) that is elected or
appointed to run a specific aspect of the chapter.
 & Every member is a little. A little is the person that a big has
guided through the pledging process
 & Event at the end of the semester in which the completion of each
member’s contract is reviewed by the chapter
 & A member who has completed the initiation ceremony, but not the
induction ceremony. These members do not have the full privilege of a
brother
 & A person who is interested in joining APO, but is not yet a pledge
 & Request for approval of community service hours

p.20p.80

DNS & Domain Name System
GAE & Google App Engine
SQL & Structured Query Language
SSL & Secure Socket Layer
WSGI & Web Server Gateway Interface

