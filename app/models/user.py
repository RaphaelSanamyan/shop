from __future__ import annotations

from typing import List

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError

from app.db import DB as db


class User(db.Model):
    __tablename__: str = "User"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(32))

    def __repr__(self) -> str:
        return self.username

    @staticmethod
    def is_exists_username(username: str) -> bool:
        return db.session\
                   .query(User.id).\
                   filter_by(username=username)\
                   .scalar() is not None

    @staticmethod
    def is_exists_email(email: str) -> bool:
        return db.session\
                   .query(User.id)\
                   .filter_by(email=email)\
                   .scalar() is not None

    def commit(self) -> None:
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def login(email: str, password: str) -> bool:
        return db.session\
                   .query(User.id)\
                   .filter_by(email=email, password=password)\
                   .scalar() is not None
