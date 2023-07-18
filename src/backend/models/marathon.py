from src.backend import db
from marshmallow import Schema, fields
import math
from bs4 import BeautifulSoup

marathon_athlete = db.Table(
    "marathon_athlete",
    db.Column("MarathonEvent_id", db.Integer, db.ForeignKey("MarathonEvents.id")),
    db.Column("Athletes_id", db.Integer, db.ForeignKey("Athletes.id")),
)


class MarathonDataHTML(BeautifulSoup):
    """Represents One Page of Marathon Results"""

    def __init__(self, html_file_data: bytes, marathon, gender: str):
        super().__init__(html_file_data, "html.parser")
        self.marathon_id = marathon.id
        self.marathon = marathon
        self.gender = gender


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

    async def _get_results_html(self, session, gender=None) -> bytes:
        page = 1
        url = f"https://chicago-history.r.mikatiming.com/2015/?page=1&event=ALL_EVENT_GROUP_{str(self.year)}&lang=EN_CAP&pid=search&pidp=start"
        if gender:
            url = f"https://chicago-history.r.mikatiming.com/2015/?page={page}&event={self.web_id}&lang=EN_CAP&num_results=25&pid=list&pidp=start&search%5Bsex%5D={gender}&search%5Bage_class%5D=%25"
        html = None
        async with session.get(url) as response:
            html = await response.read()
        return MarathonDataHTML(html, self, gender)

    async def get_male_results_html(self, session) -> bytes:
        return await self._get_results_html(session, gender="M")

    async def get_results_html(self, session) -> bytes:
        return await self._get_results_html(session)

    async def get_female_results_html(self, session) -> bytes:
        return await self._get_results_html(session, gender="W")

    async def get_male_and_female_results(self, session) -> dict[str, MarathonDataHTML]:
        return {
            "M": await self.get_male_results_html(session),
            "W": await self.get_female_results_html(session),
        }

    def get_num_of_result_pages(self) -> int:
        return math.ceil(self.num_athletes / 1000)


class MarathonSchema(Schema):
    id = fields.Number()
    year = fields.Number()
    num_athletes = fields.Number()
    num_athletes_male = fields.Number()
    num_athletes_female = fields.Number()
