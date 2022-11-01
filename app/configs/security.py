from flask import Flask
from flask_security import Security, SQLAlchemyUserDatastore
from app.configs.sqlalchemy import db
from app.models.user import User
from app.models.role import Role

security = Security()

def init_app(app: Flask):
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore, register_blueprint=False)