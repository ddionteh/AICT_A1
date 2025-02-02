from flask import Flask
from app.config.config import get_config_by_name
from app.initialize_functions import initialize_db, initialize_swagger
from app.modules.main.route import main_bp  # Import the main blueprint

def create_app(config=None) -> Flask:
    """
    Create a Flask application.

    Args:
        config: The configuration object to use.

    Returns:
        A Flask application instance.
    """
    app = Flask(__name__)

    # If a config is passed, load it
    if config:
        app.config.from_object(get_config_by_name(config))

    # Initialize the database and other extensions
    initialize_db(app)

    # Register blueprints (Pass `main_bp` here and any other blueprints you want to register)
    from app.initialize_functions import initialize_route
    initialize_route(app, main_bp)  # You can pass more blueprints if needed

    # Initialize Swagger
    initialize_swagger(app)

    return app

