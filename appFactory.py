# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)

    # Database Configuration
    username = 'root'
    password = 'EcMySQL0512173513A!'
    hostname = 'localhost'
    database_name = 'NutriBotUserLoginInfo'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{username}:{password}@{hostname}/{database_name}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    bcrypt.init_app(app)

    # Register Blueprints
    from createAuth import create_auth_blueprint
    from login import login_blueprint
    app.register_blueprint(create_auth_blueprint)
    app.register_blueprint(login_blueprint)

    return app
