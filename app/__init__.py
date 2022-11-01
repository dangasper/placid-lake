from flask import Flask
from app.configs import load_config, minify, bootstrap5, sqlalchemy, init_db_command, session, loginmanager, security, csrf
from app import routes

def create_app():
    app = Flask(__name__)
    load_config.init_app(app)
    minify.init_app(app)
    bootstrap5.init_app(app)
    routes.init_app(app)
    sqlalchemy.init_app(app)
    init_db_command.init_app(app)
    session.init_app(app)
    security.init_app(app)
    loginmanager.init_app(app)
    csrf.init_app(app)

    @app.before_first_request
    def init_initial_db():
        init_db_command.init_db()

    return app