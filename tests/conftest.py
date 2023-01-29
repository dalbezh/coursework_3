from unittest.mock import MagicMock

import pytest

from app.dao.director import DirectorDAO
from app.dao.genre import GenreDAO
from app.dao.model.director import Director
from app.dao.model.genre import Genre
from app.dao.model.movie import Movie
from app.dao.movie import MovieDAO
from app.setup_db import db


@pytest.fixture()
def director_dao():
    """
    Фикстура с мокированием методов для DirectorDAO
    """
    director_dao = DirectorDAO(db.session)

    director_1 = Director(id=1, name="TEST Director 1")
    director_2 = Director(id=2, name="TEST Director 2")
    director_3 = Director(id=3, name="TEST Director 3")

    directors = {
        1: director_1,
        2: director_2,
        3: director_3
    }

    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.get_all = MagicMock(return_value=directors.values())
    director_dao.create = MagicMock(return_value=director_3)
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock(return_value=director_1)

    return director_dao


@pytest.fixture()
def genre_dao():
    """
    Фикстура с мокированием методов для GenreDAO
    """
    genre_dao = GenreDAO(db.session)

    genre_1 = Genre(id=1, name="TEST Genre 1")
    genre_2 = Genre(id=2, name="TEST Genre 2")
    genre_3 = Genre(id=3, name="TEST Genre 3")

    genres = {
        1: genre_1,
        2: genre_2,
        3: genre_3
    }

    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.get_all = MagicMock(return_value=genres.values())
    genre_dao.create = MagicMock(return_value=genre_3)
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao


@pytest.fixture()
def movie_dao():
    """
    Фикстура с мокированием методов для MovieDAO
    """
    movie_dao = MovieDAO(db.session)

    movie_1 = Movie(id=1, title="TEST Movie 1", description="description 1",
                    trailer="YouTube Link", year=2001, rating=7.0, genre_id=1, director_id=1)
    movie_2 = Movie(id=2, title="TEST Movie 2", description="description 2",
                    trailer="YouTube Link", year=2002, rating=8.0, genre_id=2, director_id=2)
    movie_3 = Movie(id=3, title="TEST Movie 3", description="description 3",
                    trailer="YouTube Link", year=2003, rating=9.0, genre_id=3, director_id=3)

    movies = {
        1: movie_1,
        2: movie_2,
        3: movie_3
    }

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=movies.values())
    movie_dao.create = MagicMock(return_value=movie_3)
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao
