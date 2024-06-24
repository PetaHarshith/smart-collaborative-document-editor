from pymongo import MongoClient  # Import MongoClient to interact with MongoDB
from werkzeug.security import generate_password_hash, check_password_hash  # Import functions to hash and check passwords
import os  # Import os module to access environment variables

client = MongoClient(os.getenv('MONGO_URI'))  # Connect to MongoDB using the URI from environment variables
db = client.get_database('your_db_name')  # Get the specific database from MongoDB
user_collection = db.get_collection('users')  # Get the collection for users in the database

class User:
    @staticmethod
    def create_user(username, password):  # Static method to create a new user
        password_hash = generate_password_hash(password)  # Hash the user's password
        user_collection.insert_one({'username': username, 'password': password_hash})  # Insert the new user into the collection
    
    @staticmethod
    def find_user_by_username(username):  # Static method to find a user by username
        return user_collection.find_one({'username': username})  # Return the user document if found
    
    @staticmethod
    def check_password(user, password):  # Static method to check if the password is correct
        return check_password_hash(user['password'], password)  # Return True if the password matches the hash
