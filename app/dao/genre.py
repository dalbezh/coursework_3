from app.config import Config
from app.dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, id):
        return self.session.query(Genre).filter(Genre.id == id).one()

    def get_all(self, page):
        if page:
            return self.session.query(Genre).\
                paginate(page=page, per_page=Config.ELEMENTS_ON_PAGE, max_per_page=Config.MAX_PAGE).items
        return self.session.query(Genre).all()

    def create(self, data):
        genre = Genre(**data)
        self.session.add(genre)
        self.session.commit()
        return genre

    def update(self, genre):
        self.session.add(genre)
        self.session.commit()
        return genre

    def delete(self, id):
        genre = self.get_one(id)
        self.session.delete(genre)
        self.session.commit()