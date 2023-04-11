# Add any model classes for Flask-SQLAlchemy here
from app import db

class Movie(db.Model):

    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    poster = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)

    def __init__(self, title, description, poster):
        self.title = title
        self.description = description
        self.poster = poster
