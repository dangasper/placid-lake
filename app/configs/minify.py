from flask import Flask
from flask_minify import Minify

def init_app(app: Flask):
    Minify(app=app, html=True, js=True, cssless=True)
