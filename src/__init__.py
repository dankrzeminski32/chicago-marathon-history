from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Globally accessible libraries
db = SQLAlchemy()

def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')
    # Initialize Plugins
    db.init_app(app)

    with app.app_context():
        # Import blueprints and modules
        from src.utils import cli

        # Register Blueprints
        app.register_blueprint(cli.db_commands_bp)

        return app