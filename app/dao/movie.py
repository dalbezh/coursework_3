from app.config import Config
from app.dao.model.director import Director
from app.dao.model.genre import Genre
from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, id):
        return self.session.query(Movie).filter(Movie.id == id).one()

    def get_all(self, status, page):
        if status == "new" and page:
            return self.session.query(Movie).order_by(Movie.year.desc()).\
                paginate(page=page, per_page=Config.ELEMENTS_ON_PAGE, max_per_page=Config.MAX_PAGE).items
        elif status == "new":
            return self.session.query(Movie).order_by(Movie.year.desc()).all()
        elif page:
            return self.session.query(Movie).\
                paginate(page=page, per_page=Config.ELEMENTS_ON_PAGE, max_per_page=Config.MAX_PAGE).items
        return self.session.query(Movie).all()

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, id):
        movie = self.get_one(id)
        self.session.delete(movie)
        self.session.commit()
