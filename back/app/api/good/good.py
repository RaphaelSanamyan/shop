from typing import List, Optional

from flask_restplus import Resource

from app.api.good.models import good_with_id, good_model
from app.api.good.namespace import GOOD_NAMESPACE as api
from app.api.responses import get_codes
from app.models.good import Good

from app.query.controller import mark_categories


@api.route('/')
class Goods(Resource):
    @api.marshal_list_with(good_with_id, mask=None)
    @api.doc(responses=get_codes(200))
    def get(self):
        return Good.all()

    @api.expect(good_model, validate=True)
    @api.doc(responses=get_codes(200, 409))
    def post(self):
        categories: List[str] = api.payload.pop("categories")
        good: Good = mark_categories(Good(**api.payload), categories)
        return "success" if good.commit() else api.abort(409)


@api.route('/<id>')
@api.doc(params={"id": "id"})
class GoodsById(Resource):
    @api.doc(responses=get_codes(200, 404))
    def delete(self, id: int):
        return "success" if Good.delete(id=id) else api.abort(404)

    @api.expect(good_model)
    @api.doc(params={"id": "id"}, responses=get_codes(200, 404))
    def put(self, id: int):
        good: Optional[Good] = Good.first(id=id)
        good.update(**api.payload) if good else api.abort(404)
        return "success"

    @api.marshal_with(good_with_id, mask=None)
    @api.doc(responses=get_codes(200, 404))
    def get(self, id: int):
        good: Optional[Good] = Good.first(id=id)
        return good if good else api.abort(404)
