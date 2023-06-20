import pytest

from app.services.director import DirectorService


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        """
        Тест одного режиссера
        """
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id is not None
        assert director.name == "TEST Director 1"

    def test_get_all(self):
        """
        Тест всех режиссеров
        """
        directors = self.director_service.get_all(page=1)
        assert directors is not None
        assert len(directors) > 1

    def test_create(self):
        """
        Тест по созданию режиссера
        """
        data = {
            "id": 3,
            "name": "TEST Director 3"
        }

        director = self.director_service.create(data)
        assert director.id is not None

    def test_delete(self):
        """
        Тест по удалению режиссера
        """
        delete_test = self.director_service.delete(1)
        assert delete_test is None

    def test_update(self):
        """
        Тест по обновлению данных о режиссере
        """
        data = {
            "id": 1,
            "name": "TEST Director NEW"
        }
        update_test = self.director_service.update(data)
        assert update_test is None
