from flask_restplus import fields

from flask_restplus.model import Model
from app.api.auth.namespace import AUTH_NAMESPACE as api

registration_model: Model = api.model("registration", {
    "firstName": fields.String(),
    "lastName": fields.String(),
    "login": fields.String(),
    "email": fields.String(),
    "password": fields.String()
})

login_model: Model = api.model("login", {
    "login": fields.String(),
    "password": fields.String()
})
