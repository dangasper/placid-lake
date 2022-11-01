from flask import Flask
from flask_session import Session

sess = Session()

def init_app(app: Flask):
    sess.init_app(app)