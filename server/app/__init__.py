__version__ = '0.1.0'

from flask import Flask
from flask_migrate import Migrate

from backend import routes
from backend.models import db
from config import Config, Development, Production

migrate = Migrate()
def create_app(config_class=Development):
    app = Flask(__name__)
    app.config.from_object(config_class)
    routes.init_app(app)
    db.init_app(app)
    migrate.init_app(app=app, db=db)

    return app

