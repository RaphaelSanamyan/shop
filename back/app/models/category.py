from __future__ import annotations

from typing import List

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError

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

    def __repr__(self):
        return self.name

    def commit(self) -> bool:
        db.session.add(self)
        try:
            db.session.commit()
            return True
        except IntegrityError:
            return False

    @staticmethod
    def all() -> List[Category]:
        return Category.query.all()

    @staticmethod
    def first(**kwargs) -> Category:
        return Category.query.filter_by(**kwargs).first()

    @staticmethod
    def delete(**kwargs) -> bool:
        try:
            db.session.delete(Category.query.filter_by(**kwargs).first())
            db.session.commit()
            return True
        except UnmappedInstanceError:
            return False
