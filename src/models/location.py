from src.extensions import db
from src.models import BaseModel


# ეს მოდელი ყველაზე ზემოთ იმიტომაა, რომ პრობლემა მქონდა Location-თან
# როდესაც ვუთითებდი foreign_keys-ს ვერ აღიქვამდა LocationConnection-ს
class LocationConnection(BaseModel, db.Model):
    __tablename__ = 'location_connections'

    id = db.Column(db.Integer, primary_key=True)
    located_from_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    located_with_id = db.Column(db.Integer, db.ForeignKey("locations.id"))
    connection_type_id = db.Column(db.Integer, db.ForeignKey('connection_types.id'))

    located_from = db.relationship('Location', foreign_keys=located_from_id, back_populates="connection_from")
    located_with = db.relationship('Location', foreign_keys=located_with_id, back_populates="connection_with")
    connection_type = db.relationship('ConnectionType', foreign_keys=connection_type_id)

    def __repr__(self):
        return f'{self.located_from} -> {self.connection_type} -> {self.located_with}'


class Location(BaseModel, db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    period = db.Column(db.String)
    description = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    # ლოკაციის ტიპები
    types = db.relationship("Type", secondary="location_types", backref="locations")

    # ლოკაციასთან დაკავშირებული სახელები
    relations = db.relationship("LocationRelation", backref="location")

    # ლოკაციის კავშირები
    connection_with = db.relationship("LocationConnection", back_populates="located_from", foreign_keys=LocationConnection.located_from_id)
    connection_from = db.relationship("LocationConnection", back_populates="located_with", foreign_keys=LocationConnection.located_with_id)

    # ლოკაციის ბიბლიოგრააფიები
    bibliographies = db.relationship("Bibliography", secondary="location_bibliographies", backref="locations")

    # ლოკაციის ბმულები
    links = db.relationship("Link", secondary="location_links", backref="locations")

    def __repr__(self):
        return f'{self.name}'


class Type(BaseModel, db.Model):
    __tablename__ = 'types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    def __repr__(self):
        return f'{self.name}'


class LocationType(BaseModel, db.Model):
    __tablename__ = 'location_types'

    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    type_id = db.Column(db.Integer, db.ForeignKey('types.id'))


class LocationRelation(BaseModel, db.Model):
    __tablename__ = 'location_relations'

    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    name = db.Column(db.String, nullable=False)
    period = db.Column(db.String)
    text = db.Column(db.String)

    def __repr__(self):
        return f'{self.name}'


class ConnectionType(BaseModel, db.Model):
    __tablename__ = 'connection_types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    def __repr__(self):
        return f'{self.name}'
