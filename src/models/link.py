from src.extensions import db
from src.models import BaseModel


class Link(BaseModel, db.Model):
    __tablename__ = 'links'

    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    title = db.Column(db.String)
    link = db.Column(db.String)

    location = db.relationship("Location", back_populates="links")

    def __init__(self, location_id, title, link):
        self.location_id = location_id
        self.title = title
        self.link = link

    def __repr__(self):
        return f"{self.title} - {self.link} (Link)"
