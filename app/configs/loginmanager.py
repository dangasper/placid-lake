from flask import Flask
from flask_login import LoginManager

login_manager = LoginManager()

def init_app(app: Flask):
    login_manager.init_app(app)