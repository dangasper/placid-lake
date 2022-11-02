from flask import Flask, current_app, request
from app.configs import load_config, minify, bootstrap5, sqlalchemy, init_db_command, session, loginmanager, security, csrf, app_log
from app import routes
from datetime import datetime as dt
import logging
import os

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
    app_log.init_app(app)


    @app.after_request
    def after_request(response):
        """ Logging after every request. """
        logger = logging.getLogger("app.access")
        logger.info(
            "%s [%s] %s %s %s %s %s %s %s",
            request.remote_addr,
            dt.utcnow().strftime("%d/%b/%Y:%H:%M:%S.%f")[:-3],
            request.method,
            request.path,
            request.scheme,
            response.status,
            response.content_length,
            request.referrer,
            request.user_agent,
        )
        return response


    return app