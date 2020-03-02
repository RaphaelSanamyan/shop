from app.db import DB as db
from sqlalchemy import UniqueConstraint
from sqlalchemy.exc import IntegrityError


class Busket(db.Model):
    __tablename__ = "Busket"
    __table_args__ = (UniqueConstraint(
        'user_id',
        'good_id',
        name='unique_user_good'),)
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("User.id"))
    good_id = db.Column(db.Integer, db.ForeignKey("Good.id"))
    amount = db.Column(db.Integer)

    def commit(self) -> bool:
        db.session.add(self)
        try:
            db.session.commit()
            return True
        except IntegrityError:
            return False
