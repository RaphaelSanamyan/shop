from typing import Dict

from flask_jwt_extended import create_access_token
from flask_restplus import Resource

from app.api.auth.models import login_model, registration_model
from app.api.auth.namespace import AUTH_NAMESPACE as api
from app.api.responses import get_codes
from app.models.user import User


@api.route('/sign-up')
class Auth(Resource):
    @api.expect(registration_model, validate=True)
    @api.doc(responses=get_codes(200, 409))
    def post(self):
        if User.is_exists_username(api.payload.get("username")):
            return api.abort(409, "That username is taken. Try another.")

        if User.is_exists_email(api.payload.get("email")):
            return api.abort(409, "That email is taken. Try another.")

        User(**api.payload).commit()
        return create_access_token(identity=api.payload.get("username"))


@api.route('/sign-in')
class Login(Resource):
    @api.expect(login_model, validate=True)
    @api.doc(responses=get_codes(200, 401))
    def post(self):
        if User.login(**api.payload):
            return create_access_token(identity=api.payload.get("username"))
        api.abort(401, "Wrong email or password.")
