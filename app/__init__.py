from flask import Flask
from app.configs import load_config, minify, bootstrap5
from app import routes


def create_app():
    app = Flask(__name__)
    load_config.init_app(app)
    minify.init_app(app)
    bootstrap5.init_app(app)
    routes.init_app(app)
    return app