from flask import Flask
import os

def init_app(app: Flask, test_config=None):
    app.config.from_mapping(
        SECRET_KEY = 'secret135',
        BOOTSTRAP_SERVE_LOCAL = False,
        BOOTSTRAP_BOOTSWATCH_THEME = 'slate',
        SECURITY_PASSWORD_SALT = 'dev135',
        SECURITY_PASSWORD_HASH = 'pbkdf2_sha512',
        SECURITY_TRACKABLE = True,
        SQLALCHEMY_DATABASE_URI = 'sqlite:///poamtrkr.db',
        SESSION_TYPE = 'filesystem',
        SESSION_FILE_DIR = 'instance',
        SESSION_PERMANENT = False,
    )
    
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
        
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass