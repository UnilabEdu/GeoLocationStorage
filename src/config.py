from os import path


class Config(object):
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))
    SECRET_KEY = 'SECRET'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(BASE_DIRECTORY, "database.sqlite")
