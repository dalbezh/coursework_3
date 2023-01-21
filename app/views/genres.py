from flask import request
from flask_restx import Resource, Namespace

from app.container import genre_service
from app.dao.model.genre import GenreSchema

genre_ns = Namespace('genres')

genre_schema = GenreSchema()


@genre_ns.route('/')
class GenresViews(Resource):
    def get(self):
        """
        Все жанры
        + Квери параметр page
        """
        page = request.args.get("page", type=int)
        genres = genre_service.get_all(page)
        return genre_schema.dump(genres, many=True), 200


@genre_ns.route('/<int:id>/')
@genre_ns.doc(params={'id': 'ID жанра'},
              responses={
                  200: 'Success',
                  404: 'No data'
              }
              )
class GenreViews(Resource):
    def get(self, id: int):
        """
        Выдаёт жанр по id
        """
        try:
            genre = genre_service.get_one(id)
            return genre_schema.dump(genre), 200
        except Exception as ex:
            return str(ex), 404
