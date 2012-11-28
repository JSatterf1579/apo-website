from flask import flash, url_for, redirect, request
from google.appengine.ext import db

from models import SetupModel

from application.accounts.models import UserRoleModel, RoleModel
from application.members.models import FamilyModel

from application.accounts.accounts import create_user, find_users

from application import app

import os

@app.route('/setup')
def setup():
        """
        This view will check the datastore for
        a SetupModel entity with the same
        version id as this instance.

        If the entity exists it will
        redirect the user to the homepage.

        Otherwise it will create some default
        data.

        WARNING: This is simply a convenience
        method. It will also clear out all
        data for all versions!!

        It will need to be changed in subsequent versions
        """
        
        query = SetupModel.all()
        query.filter('version =', os.environ['CURRENT_VERSION_ID'])

        if query.count() == 0:
                # the app hasn't been setup yet
            #db.delete(db.Entry.all(keys_only=True))
                
                boehms = FamilyModel(name='boehms')
                boehms.put()
                snm = FamilyModel(name='s & m')
                snm.put()
                newpham = FamilyModel(name='new pham')
                newpham.put()

                default_users = []
                default_users.append(create_user('Devin',
                                                'Schwab',
                                                'dts34',
                                                'default',
                                                family=boehms.key(),
                                                avatar='digidevin@gmail.com'))
                default_users.append(create_user('Jon',
                                                'Chan',
                                                'jtc77',
                                                'default'))
                default_users.append(create_user('Zach',
                                                 'Zanes',
                                                 'zzz111',
                                                 'password'))
                default_users.append(create_user('Zach',
                                                 'Zaney',
                                                 'zzz222',
                                                 'password1@'))
                default_users.append(create_user('Adam',
                                                 'Min',
                                                 'admin',
                                                 'password'))
                
                webmaster_role = RoleModel(name='webmaster', desc='administrator for the website')
                webmaster_role.put()
                brother_role = RoleModel(name='brother', desc='general brother in the chapter')
                brother_role.put()
                pledge_role = RoleModel(name='pledge', desc='pledge in the chapter')
                pledge_role.put()
                neophyte_role = RoleModel(name='neophyte', desc='neophyte in the chapter')
                neophyte_role.put()
        
    
                #default_users = find_users()
                urole1 = UserRoleModel(user=default_users[0].key(), role=webmaster_role.key())
                urole2 = UserRoleModel(user=default_users[0].key(), role=brother_role.key())
                urole3 = UserRoleModel(user=default_users[1].key(), role=webmaster_role.key())
                urole4 = UserRoleModel(user=default_users[1].key(), role=webmaster_role.key())
                urole5 = UserRoleModel(user=default_users[2].key(), role=brother_role.key())
                urole6 = UserRoleModel(user=default_users[4].key(), role=webmaster_role.key())


                urole1.put()
                urole2.put()
                urole3.put()
                urole4.put()
                urole5.put()
                urole6.put()

                version = SetupModel(version=os.environ['CURRENT_VERSION_ID'])
                version.put()

                flash('Setup the application!', 'success')

        else:
                flash('Application is already setup', 'error')

        return redirect('/')