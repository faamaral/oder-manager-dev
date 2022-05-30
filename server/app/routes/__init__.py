from backend.routes.index import bp

def init_app(app):
    app.register_blueprint(bp)