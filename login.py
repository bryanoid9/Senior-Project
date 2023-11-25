# login.py
from flask import Blueprint, request, jsonify, render_template
from models import User
from appFactory import bcrypt
from flask_bcrypt import check_password_hash

login_blueprint = Blueprint('login_blueprint', __name__)

@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.json
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            # User exists and password is correct
            return jsonify({'success': True, 'redirect': '/welcome'})
        else:
            # User doesn't exist or password is incorrect
            return jsonify({'success': False, 'message': 'Invalid username or password'}), 401
    
    # For GET request, render the login page
    return render_template('login.html')

@login_blueprint.route('/')
def index():
    # Redirects to the login page
    return render_template('login.html')

@login_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')