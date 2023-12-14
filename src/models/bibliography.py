from src.extensions import db
from src.models import BaseModel


class Bibliography(BaseModel, db.Model):
    __tablename__ = 'bibliographies'

    id = db.Column(db.Integer, primary_key=True)
    abbreviation = db.Column(db.String)
    author = db.Column(db.String)
    title = db.Column(db.String)
    publisher = db.Column(db.String)
    year = db.Column(db.Integer)
    location = db.Column(db.String)
    language = db.Column(db.String)
    comment = db.Column(db.String)

    def __repr__(self):
        return f'{self.title} - {self.author} (bibliography)'


class LocationBibliography(BaseModel, db.Model):
    __tablename__ = 'location_bibliographies'

    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    bibliography_id = db.Column(db.Integer, db.ForeignKey('bibliographies.id'))
