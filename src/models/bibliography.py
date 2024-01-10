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

    def __init__(self, abbreviation, author=None, title=None, publisher=None, year=None, location=None, language=None, comment=None):
        self.abbreviation = abbreviation
        self.author = author
        self.title = title
        self.publisher = publisher
        self.year = year
        self.location = location
        self.language = language
        self.comment = comment

    def __repr__(self):
        return f'{self.abbreviation} - {self.title} - {self.author}'


class LocationBibliography(BaseModel, db.Model):
    __tablename__ = 'location_bibliographies'

    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    bibliography_id = db.Column(db.Integer, db.ForeignKey('bibliographies.id'))

    def __init__(self, location_id, bibliography_id):
        self.location_id = location_id
        self.bibliography_id = bibliography_id
