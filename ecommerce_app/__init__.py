from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev-unsafe-secret-key"

    from ecommerce_app.routes.store import store_bp

    app.register_blueprint(store_bp)
    return app
