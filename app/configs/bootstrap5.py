from flask import Flask
from flask_bootstrap import Bootstrap5

bootstrap = Bootstrap5()

def init_app(app: Flask):
    bootstrap.init_app(app)