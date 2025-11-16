from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

def create_app():
    # Get base directory paths
    base_dir = os.path.abspath(os.path.dirname(__file__))
    parent_dir = os.path.dirname(base_dir)

    # Initialize Flask app with correct template/static locations
    app = Flask(
        __name__,
        static_folder=os.path.join(parent_dir, "static"),
        template_folder=os.path.join(parent_dir, "templates")
    )

    # Use SECRET_KEY from .env (fallback to a development key)
    app.secret_key = os.getenv("SECRET_KEY", "dev-secret-key")

    # Register blueprints
    from app.main import main_bp
    app.register_blueprint(main_bp)

    return app
