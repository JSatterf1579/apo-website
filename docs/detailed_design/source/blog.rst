:mod:`application.blog` -- Blog Post Package
============================================
Classes
*******

.. module:: blog.blog

.. class:: BlogPost(object)
    
   The BlogPost class will allow :term:`brother`s to create and comment on blog posts.
   It contains the information about specific service events in the datastore.
   
Module Functions
****************    

.. function:: blog.blog.createBlog

   This method is a factory method for service events.
   
.. function:: blog.blog.deleteComment

   Removes a comment from the current BlogPost

:mod:'serviceEvents.models' -- Service Event related Models
-----------------------------------------------------------   

.. method:: Post(title, datetime, text, author)

   Creates a new Post entity

   :param title: Title of Blog post
   :type title: unicode

   :param datetime: Date and time of posting
   :type datetime: datetime.datetime

   :param text: Content of post
   :type text: unicode

   :param author: User that made this post
   :type author: application.models.User
   
.. method:: Comment(post, datetime, author, text)

   Creates a new Comment entity

   :param post: Post this comment is associated with
   :type post: application.models.Post

   :param datetime: Date and time of comment
   :type datetime: datetime.datetime

   :param author: User that posted this comment
   :type author: application.models.User

   :param text: Content of comment
   :type text: unicode   

:mod:`blog.views` -- Blog related views
--------------------------------------------------------

.. class:: blogView()

The blogView is used to provide the view for the blog.
   This view responds to get and post requests
  :post: causes the view to store the submitted blog or comment information to the datastore
  :get: displays the create or submit blog forms
This view uses a template
  :Template: application.blog.blogTemplate()
    
:mod:`blog.forms` -- Blog related forms
--------------------------------------------------------  

.. class:: CreateBlogForm(Form)

This form contains the fields for filling out the parameters of a blog in conjunction with
blog.blog.createBlog

   .. method:: CreateBlogForm(title, blog)
   The CreateBlogForm method is used to create a blog form, which in turn is used to create a BlogPost
   
   :param title: Title of the blog post
   :type title: unicode
   :param blog: Content of the blog post
   :type blog: unicode
       
   :rtype: Form instance
   
   .. method:: CreateCommentForm(comment)
   The CreateCommentForm method is used to create a comment form, which is used to create a Comment
   
   :param comment: Comment to be posted on the blog
   :type comment: unicode
       
   :rtype: Form instance
   
:mod:`blog.templates` -- Blog related templates
----------------------------------------------------------------

.. class:: BlogTemplate()

Used to display blog posts, comments, blog post form, and comment form. 
.. class:: blogTemplate()
Used to display blog posts, blog creation form, and comment creation form. 
   :Requires: application.blog.CreateBlogForm()
   :Requires: application.blog.CreateCommentForm()
Extends  
   :extends: MainTemplate
   :extends: blogView()