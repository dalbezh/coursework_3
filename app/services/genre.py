from app.dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, id):
        return self.dao.get_one(id)

    def get_all(self, page):
        return self.dao.get_all(page)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        id = data.get("id")
        genre = self.get_one(id)
        genre.name = data.get("name")
        self.dao.update(genre)

    def delete(self, id):
        self.dao.delete(id)