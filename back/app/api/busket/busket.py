from flask_restplus import Resource

from app.api.busket.models import item_amount, item_model, item_with_id
from app.api.busket.namespace import BUSKET_NAMESPACE as api
from app.api.responses import get_codes
from app.models.busket import Busket


@api.route("/")
class Buskets(Resource):
    @api.expect(item_model, validate=True)
    @api.doc(responses=get_codes(200, 409))
    def post(self):
        return "success" if Busket(**api.payload).commit else api.abort(409)


@api.route("/<item_id>")
class BusketsByItemId(Resource):
    @api.expect(item_amount, validate=True)
    @api.doc(responses=get_codes(200))
    def put(self, item_id):
        Busket.query.filter_by(id=item_id).first().update(api.payload["amount"])
        return "success"

    @api.doc(responses=get_codes(200, 404))
    def delete(self, item_id):
        return "success" if Busket.delete(id=item_id) else api.abort(404)

@api.route("/<user_id>")
class BusketsByUserId(Resource):
    @api.marshal_with(item_with_id, mask=None)
    @api.doc(responses=get_codes(200, 404))
    def get(self, user_id: str):
        busket = Busket.query.filter_by(user_id=user_id).all()
        return busket if busket else api.abort(404)
