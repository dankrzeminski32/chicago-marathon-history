from src.backend import db
from src.backend.constants import SEX
from marshmallow import Schema, fields


class Athlete(db.Model):
    """Data model for our Chicago Marathon Athletes"""

    __tablename__ = "Athletes"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), unique=False, nullable=False)
    last_name = db.Column(db.String(100), unique=False, nullable=False)
    country = db.Column(db.String(100), unique=False, nullable=True)
    gender = db.Column(db.SmallInteger, server_default=str(SEX.NOT_KNOWN.value))
    results = db.relationship("Result", backref="athlete")

    def __repr__(self):
        return "Athlete(id: %s, name %s %s, gender %s)" % (self.id, self.first_name,self.last_name, self.gender)

    def __str__(self):
        return "Athlete - %s %s" % (self.first_name, self.last_name)


class AthleteSchema(Schema):
    id = fields.Number()
    first_name = fields.Str()
    last_name = fields.Str()
    gender = fields.Number()
