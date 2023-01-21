import os

PWD = os.path.abspath(os.getcwd())


class Config:
    """
    Объект конфигурации
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + PWD + '/data/movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ELEMENTS_ON_PAGE = 12
    MAX_PAGE = 100
