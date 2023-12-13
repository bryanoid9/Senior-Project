from flask import Flask, session, redirect, url_for, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from functools import wraps
import secrets
import requests  # For the chatbot functionality

db = SQLAlchemy()
bcrypt = Bcrypt()
secret_key = secrets.token_hex(16)

# Chatbot functionality
def query_gpt_turbo_chat(question, api_key):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "system", "content": "You are a knowledgeable nutritionist and fitness advisor.You want to help people achieve their fitness and health goals. Do not answer any questions that are not food, exercise, nutritional, workout related."},
                     {"role": "user", "content": question}]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error in API request: {response.status_code} - {response.text}")

# Login Required Decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login_blueprint.login'))
        return f(*args, **kwargs)
    return decorated_function
def create_app():
    app = Flask(__name__)
    app.secret_key = secret_key

    # Database Configuration
    username = 'root'
    password = 'Thestrokes12!'  # Replace with your actual MySQL password
    hostname = 'localhost'
    database_name = 'NutriBotUserLoginInfo'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{username}:{password}@{hostname}/{database_name}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    bcrypt.init_app(app)

    # Register Blueprints
 
    from createAuth import create_auth_blueprint
    from login import login_blueprint
    from features import feature_blueprint
    from main import main_blueprint
    app.register_blueprint(create_auth_blueprint)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(feature_blueprint)
    app.register_blueprint(main_blueprint)

    return app