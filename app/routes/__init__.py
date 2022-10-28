from flask import Flask
from app.routes.dashboard import bp as bp_dashboard
from app.routes.poams import bp as bp_poams

def init_app(app: Flask):
    app.register_blueprint(bp_dashboard)
    app.register_blueprint(bp_poams)