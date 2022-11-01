from .. import db

class Result(db.Model):
    """Data model for Chicago Marathon Results"""
    __tablename__ = 'Results'
    id = db.Column(db.Integer, primary_key=True)
    place_overall = db.Column(
        db.Integer,
        unique=False,
        nullable=False
    )
    place_gender = db.Column(
        db.Integer, 
        nullable=False
    )
    finish_time = db.Column(
        db.String(100),
        nullable=False
    )
    bib = db.Column(
        db.String(100),
        unique=False,
        nullable=False
    )
    age_group = db.Column(
        db.String(100),
        unique=False,
        nullable=False
    )
    marathon_event_id = db.Column(db.Integer, db.ForeignKey('MarathonEvents.id'))
    athlete_id = db.Column(db.Integer, db.ForeignKey('Athletes.id'))