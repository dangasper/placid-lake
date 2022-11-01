from sqlalchemy import Date
from app.configs.sqlalchemy import db

class Poam(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    poamid = db.Column(db.String(25), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    threat = db.Column(db.String(10), nullable=False)
    created = db.Column(Date, default=db.func.now())