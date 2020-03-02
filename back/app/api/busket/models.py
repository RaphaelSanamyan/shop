from flask_restplus import fields

from flask_restplus.model import Model
from .namespace import BUSKET_NAMESPACE as api

item_amount: Model = api.model("amount", {
    "amount": fields.Integer(required=True)
})

item_model: Model = api.inherit("item", item_amount, {
    "user_id": fields.Integer(required=True),
    "good_id": fields.Integer(required=True)
})

item_with_id = api.inherit("item with id", item_model, {
    "id": fields.Integer()
})
