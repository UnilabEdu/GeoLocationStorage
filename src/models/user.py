from werkzeug.security import generate_password_hash
from flask_login import UserMixin

from src.extensions import db
from src.models import BaseModel


class User(db.Model, BaseModel, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    _password = db.Column(db.String)

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    role = db.relationship('Role', uselist=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    def is_admin(self):
        return self.role.name == "admin"

    def __init__(self, username, password, role_id):
        self.username = username
        self._password = password
        self.role_id = role_id

    def __repr__(self):
        return f"User: {self.username}"


class Role(db.Model, BaseModel):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Role: {self.name}"
