from app.dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, id):
        return self.dao.get_one(id)

    def get_all(self, page):
        return self.dao.get_all(page)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        id = data.get("id")
        director = self.get_one(id)
        director.name = data.get("name")
        self.dao.update(director)

    def delete(self, id):
        self.dao.delete(id)