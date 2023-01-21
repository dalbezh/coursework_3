from flask import request
from flask_restx import Resource, Namespace

from app.container import director_service
from app.dao.model.director import DirectorSchema

director_ns = Namespace('directors')

director_schema = DirectorSchema()


@director_ns.route('/')
class DirectorsViews(Resource):
    def get(self):
        """
        Все режиссеры
        + Квери параметр page
        """
        page = request.args.get("page", type=int)
        directors = director_service.get_all(page)
        return director_schema.dump(directors, many=True), 200


@director_ns.route('/<int:id>')
@director_ns.doc(params={'id': 'ID режиссера'},
                 responses={
                     200: 'Success',
                     404: 'No data'
                 }
            )
class DirectorViews(Resource):
    def get(self, id: int):
        """
        Выдаёт режиссёра по id
        """
        try:
            director = director_service.get_one(id)
            return director_schema.dump(director), 200
        except Exception as ex:
            return str(ex), 404
