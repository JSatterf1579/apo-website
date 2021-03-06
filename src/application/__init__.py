"""
Initialize Flask app

"""

from flask import Flask
import flaskext.flask_login

app = Flask('application')
app.config.from_object('application.settings')

# login manager setup
login_manager = flaskext.flask_login.LoginManager()
login_manager.setup_app(app)
login_manager.login_view = "login" # set this to the view name

import views
import accounts.views
import members.views
import facebook.views
import blog.views
import setup.views
import photos.views
import contracts.views
import service.views