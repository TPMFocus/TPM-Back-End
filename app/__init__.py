from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import logging

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    try:
        with app.app_context():
            from app.main import models
            db.create_all()
    except Exception as e:
        logging.error(f"Failed to create tables: {e}")

    from app.main import routes
    app.register_blueprint(routes.bp)

    return app