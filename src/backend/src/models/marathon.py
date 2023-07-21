from src import db
from marshmallow import Schema, fields
import math
from bs4 import BeautifulSoup
import concurrent.futures
import requests

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
        num_athletes_male=None,
        num_athletes_female=None,
    ):
        self.year = year
        self.web_id = web_id
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

    @property
    def num_athletes(self):
        return self.num_athletes_male + self.num_athletes_female

    def _get_results_html(self, gender=None, sample=False) -> bytes:
        urls = self._create_data_urls(gender, sample=True)
        results = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for url in urls:
                futures.append(
                    executor.submit(
                        requests.get, url
                        )
                    )
            for future in concurrent.futures.as_completed(futures):
                results.append(MarathonDataHTML(future.result().content, self, gender))
        return results


    def _create_data_urls(self, gender=None, sample=False):
        urls = []
        page_count = 1
        if gender:
            if gender=="M":
                page_count = self.get_num_of_result_pages(self.num_athletes_male) if not sample else 1
            if gender=="W":
                page_count = self.get_num_of_result_pages(self.num_athletes_female) if not sample else 1
            for idx in range(1, page_count + 1):
                urls.append(f"https://chicago-history.r.mikatiming.com/2015/?page={idx}&event={self.web_id}&lang=EN_CAP&num_results=25&pid=list&pidp=start&search%5Bsex%5D={gender}&search%5Bage_class%5D=%25")
            return urls
        page_count = self.get_num_of_result_pages(self.num_athletes) if not sample else 1
        for idx in range(1, page_count):
            urls += f"https://chicago-history.r.mikatiming.com/2015/?page={idx}&event=ALL_EVENT_GROUP_{str(self.year)}&lang=EN_CAP&pid=search&pidp=start"
        return test_urls



    def get_male_results_html(self, sample=False) -> bytes:
        return self._get_results_html(gender="M", sample=sample)

    def get_results_html(self, sample=False) -> bytes:
        return self._get_results_html(sample=sample)

    def get_female_results_html(self, sample=False) -> bytes:
        return self._get_results_html(gender="W", sample=sample)

    def get_male_and_female_results(self) -> dict[str, MarathonDataHTML]:
        return {
                "M": self.get_male_results_html(sample=True),
                "W": self.get_female_results_html(sample=True)
                }

    def get_num_of_result_pages(self, num_athletes: int) -> int:
        return math.ceil(num_athletes / 500)


class MarathonSchema(Schema):
    id = fields.Number()
    year = fields.Number()
    num_athletes = fields.Number()
    num_athletes_male = fields.Number()
    num_athletes_female = fields.Number()
