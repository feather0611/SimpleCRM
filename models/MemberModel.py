from datetime import datetime as dt
from app import db


class Member(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), nullable=False)
    create_time = db.Column(db.DateTime, nullable=True)

    def __init__(self, username, create_time=dt.now()):
        self.username = username
        self.create_time = create_time

    def serialize(self):
        return {
            "pk": self.pk,
            "username": self.username,
            "create_time": str(self.create_time),
        }


