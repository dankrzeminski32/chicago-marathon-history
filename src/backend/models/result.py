from src.backend import db
from marshmallow import Schema, fields
from src.backend.models.athlete import AthleteSchema
from src.backend.models.marathon import MarathonSchema


class Result(db.Model):
    """Data model for Chicago Marathon Results"""

    __tablename__ = "Results"
    id = db.Column(db.Integer, primary_key=True)
    place_overall = db.Column(db.Integer, unique=False, nullable=False)
    place_gender = db.Column(db.Integer, nullable=False)
    finish_time = db.Column(db.Time, nullable=False)
    bib = db.Column(db.String(100), unique=False, nullable=False)
    age_group = db.Column(db.String(100), unique=False, nullable=False)
    marathon_event_id = db.Column(db.Integer, db.ForeignKey("MarathonEvents.id"))
    athlete_id = db.Column(db.Integer, db.ForeignKey("Athletes.id"))

    def __repr__(self):
        return f"Result<id: {self.id},bib: {self.bib},marathon_event_id: {self.marathon_event_id}>"

    def __str__(self):
        return f"Result for {self.id}, Place Overall: {self.place_overall}, Place Gender: {self.place_gender}"



class ResultSchema(Schema):
    id = fields.Number()
    place_overall = fields.Number()
    place_gender = fields.Number()
    finish_time = fields.Time()
    age_group = fields.Str()
    marathon_event = fields.Nested(MarathonSchema())
    athlete = fields.Nested(AthleteSchema())
