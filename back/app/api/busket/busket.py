from flask_restplus import Resource

from app.api.busket.models import item
from app.api.busket.namespace import BUSKET_NAMESPACE as api
from app.api.responses import get_codes
from app.models.busket import Busket


@api.route('/')
class Buskets(Resource):
    @api.expect(item, validate=True)
    @api.doc(responses=get_codes(200, 409))
    def post(self):
        return "success" if Busket(**api.payload).commit() else api.abort(409)
