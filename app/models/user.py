from sqlalchemy import DateTime
from app.configs.sqlalchemy import db
from app.models.rolesusers import roles_users
from flask_security import UserMixin as fsUserMixin

class User(fsUserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), unique=False, nullable=False)
    active = db.Column(db.Boolean(), default=True)
    last_login_at = db.Column(DateTime('%'))
    current_login_at = db.Column(DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))