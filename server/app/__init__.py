__version__ = '0.1.0'

from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from app import routes
from app.models import db
from config import Config, Development, Production

migrate = Migrate()
jwt = JWTManager()
def create_app(config_class=Development):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app=app, db=db)
    jwt.init_app(app)
    routes.init_app(app)

    return app

