from .. import db
from src.constants import Sex
from marshmallow import Schema, fields

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

    def __repr__(self):
       return 'Athlete(id: %s, name %s, gender %s)' % (self.id, self.name, self.gender)    
  
    def __str__(self):
       return 'Athlete - %s' % self.name

class AthleteSchema(Schema):
    id = fields.Number()
    name = fields.Str()
    gender = fields.Str()