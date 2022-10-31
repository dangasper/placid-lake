import datetime
from sqlalchemy import DateTime
from app.configs.sqlalchemy import db
from dataclasses import dataclass

@dataclass
class Poam(db.Model):

    id: int
    poamid: str
    description: str
    threat: str
    created: datetime.datetime

    id = db.Column(db.Integer, primary_key=True)
    poamid = db.Column(db.String(25), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    threat = db.Column(db.String(10), nullable=False)
    created = db.Column(DateTime, default=db.func.now())