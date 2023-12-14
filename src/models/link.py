from src.extensions import db
from src.models import BaseModel


class Link(BaseModel, db.Model):
    __tablename__ = 'links'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    link = db.Column(db.String)

    def __repr__(self):
        return f"{self.title} - {self.link} (Link)"


class LocationLink(BaseModel, db.Model):
    __tablename__ = 'location_links'

    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    link_id = db.Column(db.Integer, db.ForeignKey('links.id'))
