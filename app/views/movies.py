from flask import request
from flask_restx import Resource, Namespace

from app.container import movie_service
from app.dao.model.movie import MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()


@movie_ns.route('/')
class MoviesViews(Resource):
    def get(self):
        """
        Все фильмы
        + Квери параметры status и page
        """
        status = request.args.get("status", type=str)
        page = request.args.get("page", type=int)
        movies = movie_service.get_all(status, page)
        return movie_schema.dump(movies, many=True), 200


@movie_ns.route('/<int:id>/')
@movie_ns.doc(params={'id': 'ID фильма'},
              responses={
                  200: 'Success',
                  404: 'No data'
              }
              )
class MovieViews(Resource):
    def get(self, id: int):
        """
        Выдаёт фильм по id
        """
        try:
            movie = movie_service.get_one(id)
            return movie_schema.dump(movie), 200
        except Exception as ex:
            return str(ex), 404
