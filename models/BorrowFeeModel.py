from app import db


class BorrowFee(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    member_fk = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    borrow_fee = db.Column(db.Double, nullable=False)
    borrow_time = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.DateTime, nullable=True)

    def serialize(self):
        return {
            "pk": self.pk,
            "member_fk": self.member_fk,
            "type": self.type,
            "borrow_fee": self.borrow_fee,
            "borrow_time": self.borrow_time,
            "create_time": str(self.create_time),
        }
