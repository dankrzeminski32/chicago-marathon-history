from .. import db
from src.constants import Sex


class Athlete(db.Model):
    """Data model for our Chicago Marathon Athletes"""
    __tablename__ = 'Athletes'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(100),
        unique=False,
        nullable=False
    )
    gender = db.Column(
        db.SmallInteger,
        server_default=str(Sex.NOT_KNOWN.value)
    )
    results = db.relationship('Result', backref='athlete')