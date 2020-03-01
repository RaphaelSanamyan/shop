from __future__ import annotations

from sqlalchemy.exc import IntegrityError

from app.db import DB as db
from app.models.good_category import good_category


class Category(db.Model):
    __tablename__ = "Category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    good = db.relationship(
        "Good",
        backref="categories",
        secondary=good_category,
        lazy="dynamic"
    )

    def commit(self) -> bool:
        db.session.add(self)
        try:
            db.session.commit()
            return True
        except IntegrityError:
            return False
