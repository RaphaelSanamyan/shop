from flask_restplus import fields

from flask_restplus.model import Model
from .namespace import GOOD_NAMESPACE as api

good_model: Model = api.model("good", {
    "name": fields.String(required=True),
    "weight": fields.String(required=True),
    "description": fields.String(required=True),
    "measure": fields.String(required=True),
    "price": fields.Integer(required=True),
    "categories": fields.List(fields.String, required=True)
})

good_with_id: Model = api.inherit("good with id", good_model, {
    "id": fields.Integer()
})
