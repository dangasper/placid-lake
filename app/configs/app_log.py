from flask import Flask
from app.models.logging import LogSetup

logs = LogSetup()

def init_app(app: Flask):
    logs.init_app(app)