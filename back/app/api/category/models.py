from flask_restplus import fields

from flask_restplus.model import Model
from .namespace import CATEGORY_NAMESPACE as api

category_model: Model = api.model("category", {
    "name": fields.String(required=True)
})

category_with_id: Model = api.inherit("category with id", category_model, {
    "id": fields.Integer()
})
