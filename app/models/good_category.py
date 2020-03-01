from __future__ import annotations

from app.db import DB as db

good_category = db.Table(
    "GoodCategory",
    db.Column("fkGooodId", db.Integer, db.ForeignKey("Good.id")),
    db.Column("fkCategory", db.Integer, db.ForeignKey("Category.id"))
)
