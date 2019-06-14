import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager= LoginManager()

app = Flask(__name__)
app.config['SECRET_KEY']= 'mysecretkey'
basedir= os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' +os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)
Migrate(app,db)

login_manager.init_app(app)
login_manager.login_view= 'login'

from project.employee.views import employee_blueprints
from project.hr.views import hr_blueprints
from project.book.views import book_blueprints

app.register_blueprint(hr_blueprints, url_prefix= '/hr')
app.register_blueprint(employee_blueprints, url_prefix= '/employees')
app.register_blueprint(book_blueprints, url_prefix= '/book')
