from flask_restplus import fields

from flask_restplus.model import Model
from .namespace import GOOD_NAMESPACE as api

good_model: Model = api.model("good", {
    "name": fields.String(),
    "description": fields.String(),
    "price": fields.Integer()
})

good_by_id: Model = api.inherit("good with id", good_model, {
    "id": fields.Integer()
})
