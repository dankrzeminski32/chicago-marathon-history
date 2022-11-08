from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Globally accessible libraries
db = SQLAlchemy()

def init_app(config: object | str):
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config) #config.DevConfig
    # Initialize Plugins
    db.init_app(app)

    with app.app_context():
        # Import blueprints and modules
        from src import cli
        from src.api import athlete
        from src.api import marathon
        from src.api import result

        # Register Blueprints
        app.register_blueprint(cli.db_commands_bp)
        app.register_blueprint(athlete.athlete_api_bp)
        app.register_blueprint(marathon.marathon_api_bp)
        app.register_blueprint(result.result_api_bp)

        return app