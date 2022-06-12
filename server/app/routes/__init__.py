from app.routes.index import bp
from app.routes.auth import auth
from app.routes.product import product_bp

def init_app(app):
    app.register_blueprint(bp)
    app.register_blueprint(auth)
    app.register_blueprint(product_bp)