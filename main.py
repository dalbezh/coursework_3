from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from app.config import Config
from app.setup_db import db
from app.views.auth import auth_ns
from app.views.directors import director_ns
from app.views.genres import genre_ns
from app.views.movies import movie_ns
from app.views.users import user_ns


def create_app(config: Config) -> Flask:
    """
    Инициализация приложения
    :param config: конфигурация из app/config.py
    :return: экземпляр приложение
    """
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    return application


def configure_app(application: Flask):
    """
    Настройка приложения
    :param application: экземпляр приложения
    """
    CORS(application)
    db.init_app(application)
    api = Api(application, doc='/docs')
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


def create_table():
    """
    Создание недостающей таблицы
    """
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    create_table()
    app.run()
