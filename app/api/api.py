from flask import Blueprint
from flask_restplus import Api

from app.api.good.namespace import GOOD_NAMESPACE
from app.api.auth.namespace import AUTH_NAMESPACE


def create_api() -> Blueprint:
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api = Api(blueprint, title='honey-bunny', version="0.1")
    api.add_namespace(GOOD_NAMESPACE)
    api.add_namespace(AUTH_NAMESPACE)
    return blueprint
