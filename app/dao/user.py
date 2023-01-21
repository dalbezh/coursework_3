from app.dao.model.user import User


class UserDAO():
    def __init__(self, session):
        self.session = session

    def get_one(self, id):
        return self.session.query(User).filter(User.id == id).one()

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email == email).one()

    def get_all(self):
        return self.session.query(User).all()

    def create(self, data):
        user = User(**data)
        self.session.add(user)
        self.session.commit()
        return user

    def update(self, user):
        self.session.add(user)
        self.session.commit()
        return user

    def delete(self, id):
        user = self.get_one(id)
        self.session.delete(user)
        self.session.commit()
