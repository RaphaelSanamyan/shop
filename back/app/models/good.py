from __future__ import annotations

from typing import List

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError

from app.db import DB as db
from app.models.good_category import good_category


class Good(db.Model):
    __tablename__: str = "Good"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    weight = db.Column(db.String(64))
    description = db.Column(db.Text)
    measure = db.Column(db.String(64))
    price = db.Column(db.Float)
    category = db.relationship(
        "Category",
        backref="goods",
        secondary=good_category,
        lazy="dynamic"
    )

    def __repr__(self) -> str:
        return self.name

    def commit(self) -> bool:
        db.session.add(self)
        try:
            db.session.commit()
            return True
        except IntegrityError:
            return False

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key != "categories":
                self.__setattr__(key, value)

        db.session.commit()

    @staticmethod
    def first(**kwargs) -> Good:
        return Good.query.filter_by(**kwargs).first()

    @staticmethod
    def all() -> List[Good]:
        return Good.query.all()

    @staticmethod
    def delete(**kwargs) -> bool:
        try:
            db.session.delete(Good.query.filter_by(**kwargs).first())
            db.session.commit()
            return True
        except UnmappedInstanceError:
            return False
