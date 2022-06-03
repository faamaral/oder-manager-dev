from app.routes.index import bp
from app.routes.auth import auth

def init_app(app):
    app.register_blueprint(bp)
    app.register_blueprint(auth)