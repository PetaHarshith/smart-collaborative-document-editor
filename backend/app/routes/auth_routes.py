from flask import Blueprint, request  # Import Blueprint and request from Flask
from app.services.auth_service import AuthService  # Import AuthService for authentication logic

auth_bp = Blueprint('auth', __name__)  # Create a Blueprint for authentication routes

@auth_bp.route('/register', methods=['POST'])  # Define a route for user registration
def register():
    data = request.get_json()  # Get the JSON data from the request
    return AuthService.register(data['username'], data['password'])  # Call AuthService to register the user

@auth_bp.route('/login', methods=['POST'])  # Define a route for user login
def login():
    data = request.get_json()  # Get the JSON data from the request
    return AuthService.login(data['username'], data['password'])  # Call AuthService to login the user
