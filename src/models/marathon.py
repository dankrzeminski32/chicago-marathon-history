from .. import db

class MarathonEvent(db.Model):
    """Data model for our each chicago marathon"""
    __tablename__ = 'MarathonEvents'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    year = db.Column(
        db.Integer,
        unique=True,
        nullable=False
    )
    web_id = db.Column(
        db.String(155),
        unique=True,
        nullable=False
    )
    num_athletes = db.Column(db.Integer)
    num_athletes_male = db.Column(db.Integer)
    num_athletes_female = db.Column(db.Integer)

    def __init__(self, year, web_id, num_athletes=None, num_athletes_male=None,num_athletes_female=None):
        self.year = year
        self.web_id = web_id
        self.num_athletes=num_athletes
        self.num_athletes_male=num_athletes_male
        self.num_athletes_female=num_athletes_female