from flask import Flask
from app.routes.dashboard import bp as bp_dashboard
from app.routes.poams import bp as bp_poams
from app.routes.auth import bp as bp_auth
from app.routes.user import bp as bp_user
from app.routes.admin import bp as bp_admin

def init_app(app: Flask):
    app.register_blueprint(bp_dashboard)
    app.register_blueprint(bp_poams)
    app.register_blueprint(bp_auth)
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_admin)