from app.config import Config
from app.dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, id):
        return self.session.query(Director).filter(Director.id == id).one()

    def get_all(self, page):
        if page:
            return self.session.query(Director).\
                paginate(page=page, per_page=Config.ELEMENTS_ON_PAGE, max_per_page=Config.MAX_PAGE).items
        return self.session.query(Director).all()
    
    def create(self, data):
        director = Director(**data)
        self.session.add(director)
        self.session.commit()
        return director
    
    def update(self, director):
        self.session.add(director)
        self.session.commit()
        return director

    def delete(self, id):
        director = self.get_one(id)
        self.session.delete(director)
        self.session.commit()
