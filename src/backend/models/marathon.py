from src.backend import db
from marshmallow import Schema, fields

marathon_athlete = db.Table(
    "marathon_athlete",
    db.Column("MarathonEvent_id", db.Integer, db.ForeignKey("MarathonEvents.id")),
    db.Column("Athletes_id", db.Integer, db.ForeignKey("Athletes.id")),
)


class MarathonEvent(db.Model):
    """Data model for our each chicago marathon"""

    __tablename__ = "MarathonEvents"
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, unique=True, nullable=False)
    web_id = db.Column(db.String(155), unique=True, nullable=False)
    num_athletes = db.Column(db.Integer)
    num_athletes_male = db.Column(db.Integer)
    num_athletes_female = db.Column(db.Integer)
    results = db.relationship("Result", backref="marathon_event")
    athletes = db.relationship(
        "Athlete", secondary="marathon_athlete", backref="marathons"
    )

    def __init__(
        self,
        year,
        web_id,
        num_athletes=None,
        num_athletes_male=None,
        num_athletes_female=None,
    ):
        self.year = year
        self.web_id = web_id
        self.num_athletes = num_athletes
        self.num_athletes_male = num_athletes_male
        self.num_athletes_female = num_athletes_female

    def __repr__(self):
        return (
            "MarathonEvent(year: %s, web_id: %s, num_athletes: %s, num_athletes_female: %s, num_athletes_male: %s)"
            % (
                self.year,
                self.web_id,
                self.num_athletes,
                self.num_athletes_female,
                self.num_athletes_male,
            )
        )

    def __str__(self):
        return f"Marathon Event in {self.year}, unique id = {self.web_id}"


class MarathonSchema(Schema):
    id = fields.Number()
    year = fields.Number()
    num_athletes = fields.Number()
    num_athletes_male = fields.Number()
    num_athletes_female = fields.Number()
