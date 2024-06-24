from flask import Flask  # Import Flask to create the web application
from flask_cors import CORS  # Import CORS for Cross-Origin Resource Sharing
from flask_jwt_extended import JWTManager  # Import JWTManager for JSON Web Token handling
from flask_socketio import SocketIO  # Import SocketIO for real-time communication

def create_app():
    app = Flask(__name__)  # Create a new Flask application instance
    app.config.from_object('config.Config')  # Load configuration from the Config class
    CORS(app)  # Enable CORS for the Flask app
    JWTManager(app)  # Enable JWT handling for the Flask app
    socketio = SocketIO(app)  # Enable real-time communication with SocketIO

    from .routes.auth_routes import auth_bp  # Import authentication routes
    from .routes.doc_routes import doc_bp  # Import document routes
    app.register_blueprint(auth_bp)  # Register authentication routes with the app
    app.register_blueprint(doc_bp)  # Register document routes with the app

    return app  # Return the Flask app instance
