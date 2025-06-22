from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

db = SQLAlchemy()

class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)

    # One-to-many relationship with Appearance
    appearances = db.relationship('Appearance', back_populates='episode', cascade='all, delete-orphan')

    # Optional: guests through appearances
    guests = association_proxy('appearances', 'guest')

    def to_dict(self, only=None):
        data = {
        "id": self.id,
        "date": self.date,
        "number": self.number,
        "appearances": [appearance.to_dict() for appearance in self.appearances]
        }

        if only:
            data = {key: data[key] for key in only if key in data}

        return data


class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String, nullable=False)

    # One-to-many relationship with Appearance
    appearances = db.relationship('Appearance', back_populates='guest', cascade='all, delete-orphan')
    episodes = association_proxy('appearances', 'episode')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "occupation": self.occupation
        }

class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'))
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'))

    # Many-to-one relationships
    guest = db.relationship('Guest', back_populates='appearances')
    episode = db.relationship('Episode', back_populates='appearances')

    def to_dict(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "guest_id": self.guest_id,
            "episode_id": self.episode_id,
            "guest": self.guest.to_dict(),
            "episode": {
                "id": self.episode.id,
                "date": self.episode.date,
                "number": self.episode.number
            }
        }

    @validates('rating')
    def validate_rating(self, key, rating):
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")
        return rating
