from flask_jwt_extended import create_access_token
from flask_restplus import Resource

from app.api.auth.models import auth_response_model, login_model, \
    registration_model
from app.api.auth.namespace import AUTH_NAMESPACE as api
from app.api.responses import get_codes
from app.models.user import User


@api.route('/sign-up')
class Auth(Resource):
    @api.expect(registration_model, validate=True)
    @api.doc(responses=get_codes(409))
    @api.marshal_with(auth_response_model)
    def post(self):
        if User.is_exists_login(api.payload["login"]):
            return api.abort(409, "That login is taken. Try another.")

        if User.is_exists_email(api.payload.get("email")):
            return api.abort(409, "That email is taken. Try another.")

        user_id: int = User(**api.payload).commit.id
        identity: str = "{firstName} {lastName}".format(
            firstName=api.payload["firstName"],
            lastName=api.payload["lastName"]
        )
        return {
            "accessToken": create_access_token(identity=identity),
            "userId": user_id,
            "firstName": api.payload["firstName"],
            "lastName": api.payload["lastName"]
        }


@api.route('/sign-in')
class Login(Resource):
    @api.expect(login_model, validate=True)
    @api.doc(responses=get_codes(200, 401))
    def post(self):
        if User.log_in(**api.payload):
            return create_access_token(identity=api.payload.get("username"))
        api.abort(401, "Wrong email or password.")
