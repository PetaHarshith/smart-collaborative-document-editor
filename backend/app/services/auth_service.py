from app.models.user import User  # Import the User model
from flask_jwt_extended import create_access_token  # Import function to create JWT tokens

class AuthService:
    @staticmethod
    def register(username, password):  # Static method to register a new user
        if User.find_user_by_username(username):  # Check if the user already exists
            return {'message': 'User already exists'}, 400  # Return error if user exists
        User.create_user(username, password)  # Create a new user if they don't exist
        return {'message': 'User created successfully'}, 201  # Return success message

    @staticmethod
    def login(username, password):  # Static method to log in a user
        user = User.find_user_by_username(username)  # Find the user by username
        if not user or not User.check_password(user, password):  # Check if user exists and password is correct
            return {'message': 'Invalid credentials'}, 401  # Return error if credentials are invalid
        access_token = create_access_token(identity=username)  # Create JWT token for the user
        return {'access_token': access_token}, 200  # Return the access token
