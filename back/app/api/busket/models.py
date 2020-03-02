from flask_restplus import fields

from flask_restplus.model import Model
from .namespace import BUSKET_NAMESPACE as api

item: Model = api.model("item", {
    "user_id": fields.Integer(required=True),
    "good_id": fields.Integer(required=True),
    "amount": fields.Integer(required=True)
})
