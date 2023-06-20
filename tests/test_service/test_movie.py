import pytest

from app.services.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        """
        Тест одного фильма
        """
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None
        assert movie.trailer == "YouTube Link"

    def test_get_all(self):
        """
        Тест всех фильмов
        """
        movies = self.movie_service.get_all(status="new", page=1)
        assert movies is not None
        assert len(movies) > 1

    def test_create(self):
        """
        Тест по созданию фильма
        """
        data = {
            "id": 3,
            "title": "TEST Movie 3",
            "description": "description 3",
            "trailer": "YouTube Link",
            "year": 2003,
            "rating": 9.0,
            "genre_id": 3,
            "director_id": 3
        }

        movie = self.movie_service.create(data)
        assert movie.id is not None

    def test_delete(self):
        """
        Тест по удалению фильма
        """
        delete_test = self.movie_service.delete(1)
        assert delete_test is None

    def test_update(self):
        """
        Тест по обновлению данных о фильма
        """
        data = {
            "trailer": "RuTube Link"
        }
        update_test = self.movie_service.update(data)
        assert update_test is None
