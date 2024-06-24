import os  # Import the os module to interact with the operating system

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')  # Retrieve the secret key from environment variables for secure sessions
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')  # Retrieve the JWT secret key from environment variables for token signing
    MONGO_URI = os.getenv('MONGO_URI')  # Retrieve the MongoDB URI from environment variables for database connection
