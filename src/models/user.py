from src.extensions import db
from src.models import BaseModel
from werkzeug.security import generate_password_hash


class User(db.Model, BaseModel):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    _password = db.Column(db.String)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)
