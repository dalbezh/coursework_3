import pytest

from app.services.genre import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        """
        Тест одного жанра
        """
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id is not None
        assert genre.name == "TEST Genre 1"

    def test_get_all(self):
        """
        Тест всех жанров
        """
        genres = self.genre_service.get_all(page=1)
        assert genres is not None
        assert len(genres) > 1

    def test_create(self):
        """
        Тест по созданию жанра
        """
        data = {
            "id": 3,
            "name": "TEST Genre 3"
        }

        genre = self.genre_service.create(data)
        assert genre.id is not None

    def test_delete(self):
        """
        Тест по удалению жанра
        """
        delete_test = self.genre_service.delete(1)
        assert delete_test is None

    def test_update(self):
        """
        Тест по обновлению данных о жанре
        """
        data = {
            "name": "TEST Genre NEW"
        }
        update_test = self.genre_service.update(data)
        assert update_test is not None
