"""
Module used to scrape the official chicago marathon results website. Will be used via a command line "flask run seed"
"""
from bs4 import BeautifulSoup
import requests
from src.backend.models.marathon import MarathonEvent
from src.backend.models.athlete import Athlete
from src.backend.models.result import Result
from src.backend.services.marathon_service import MarathonEventService
import math
from src.backend.constants import SEX
from time import sleep
from random import randint
import datetime

class EventJsonParser:
    """Parses json request to get unique event ids for history scraper"""

    URL = "https://chicago-history.r.mikatiming.com/2011/index.php?content=ajax2&func=getSearchFields&options[b][lists][event_main_group]=2015&options[b][lists][event]=&options[b][lists][sex]=&options[lang]=EN_CAP&options[pid]=start"
    content = requests.get(URL).json()

    def _get_event_list(self) -> list[dict]:
        """returns raw list of events in json format

        Returns:
            list[dict]: Multiple dictionaries with year and various event (marathon,wheelchair, handcycle) info,
        """
        return self.content["branches"]["search"]["fields"]["event"]["data"]

    def _get_marathon_data(self) -> list[dict]:
        """returns raw list of marathon id's and marathon year information

        Returns:
            list[dict]: multiple dictionaries containing year and marathon id information
        """
        all_events = self._get_event_list()
        marathon_list = [v for i, v in enumerate(all_events) if i % 4 < 2]
        return marathon_list

    def get_marathon_event_ids(self) -> dict[int:MarathonEvent]:
        """parses json data and returns a user friendly list of MarathonEvent objects

        Returns:
            list[MarathonEvent]: list of MarathonEvent objects
        """
        marathon_list = self._get_marathon_data()
        parsed_marathon_events: dict[int:MarathonEvent] = {}
        for idx in range(0, len(marathon_list) - 1):
            if idx % 2 != 0:
                continue  # skips current iteration
            year = marathon_list[idx]["v"][0][-4:]
            marathon_id = marathon_list[idx + 1]["v"][0]
            parsed_marathon_events[int(year)] = MarathonEvent(int(year), marathon_id)
        return parsed_marathon_events


class HistoryMarathonScraper:
    """Scrapes Athlete data and finish times over 20 years"""

    def __init__(self):
        self.marathons: dict[
            int:MarathonEvent
        ] = EventJsonParser().get_marathon_event_ids()

    def get_parser(self, year: int, *, gender: str = None):
        if gender is None:
            URL = f"https://chicago-history.r.mikatiming.com/2015/?page=1&event=ALL_EVENT_GROUP_{str(year)}&lang=EN_CAP&pid=search&pidp=start"
        elif gender == "M" or gender == "W":
            URL = f"https://chicago-history.r.mikatiming.com/2015/?page=2&event={self.marathons[year].web_id}&lang=EN_CAP&pid=list&pidp=start&search%5Bsex%5D={gender}&search%5Bage_class%5D=%25"
        else:
            raise ValueError("Gender must be either 'M' or 'W'")

        content = requests.get(URL).content
        return BeautifulSoup(
            content, "html.parser"
        )  # If this line causes an error, run 'pip install html5lib' or install html5lib

    def _populate_num_athletes(self) -> None:
        """populates marathon objects number of athletes for a given years"""
        for key in self.marathons:
            parser: BeautifulSoup = self.get_parser(key)
            marathon: MarathonEvent = self.marathons[key]
            total_participants = parser.find(
                "li", attrs={"class": "list-group-item"}
            ).text.split()[0]
            marathon.num_athletes = int(total_participants)

    def _populate_num_female_athletes(self) -> None:
        """populates marathon objects number of female athletes for a given year"""
        for key in self.marathons:
            parser: BeautifulSoup = self.get_parser(key, gender="W")
            marathon: MarathonEvent = self.marathons[key]
            total_female_participants = parser.find(
                "li", attrs={"class": "list-group-item"}
            ).text.split()[0]
            marathon.num_athletes_female = int(total_female_participants)

    def _populate_num_male_athletes(self) -> None:
        """populates marathon objects number of male athletes for a given year"""
        for key in self.marathons:
            parser: BeautifulSoup = self.get_parser(key, gender="M")
            marathon: MarathonEvent = self.marathons[key]
            total_male_participants = parser.find(
                "li", attrs={"class": "list-group-item"}
            ).text.split()[0]
            marathon.num_athletes_male = int(total_male_participants)

    def get_marathons(self) -> dict[int:MarathonEvent]:
        """returns a list of MarathonEvent objects"""
        self._populate_num_athletes()
        self._populate_num_female_athletes()
        self._populate_num_male_athletes()
        return self.marathons


class HistoryAthleteScraper:
    def __init__(self):
        self.marathons: list[MarathonEvent] = MarathonEventService.get_all()

    def get_parser(
        self,
        marathon: MarathonEvent,
        *,
        gender: str = None,
        page: int = 1,
        sample=False,
    ):
        if gender is None:
            URL = f"https://chicago-history.r.mikatiming.com/2015/?page={page}&event=ALL_EVENT_GROUP_{str(marathon.year)}&lang=EN_CAP&pid=search&pidp=start"
        elif gender == "M" or gender == "W":
            URL = f"https://chicago-history.r.mikatiming.com/2015/?page={page}&event={marathon.web_id}&lang=EN_CAP&num_results={25 if sample else None}&pid=list&pidp=start&search%5Bsex%5D={gender}&search%5Bage_class%5D=%25"
        else:
            raise ValueError("Gender must be either 'M' or 'W'")

        content = requests.get(URL).content
        return BeautifulSoup(
            content, "html.parser"
        )  # If this line causes an error, run 'pip install html5lib' or install html5lib

    def get_data(self, sample=False) -> list[tuple]:
        all_marathon_data: list[list(tuple(Athlete, Result))] = []

        for marathon in self.marathons:
            num_pages_male = self._get_num_of_pages(marathon.num_athletes_male)
            print(num_pages_male)
            male_data = self._get_athletes_and_results(
                marathon, "M", num_pages_male, sample
            )
            print(male_data)
            all_marathon_data.append(male_data)
            num_pages_female = self._get_num_of_pages(marathon.num_athletes_female)
            print(num_pages_female)
            female_data = self._get_athletes_and_results(
                marathon, "W", num_pages_female, sample
            )
            all_marathon_data.append(female_data)
            print(
                "ALL MARATHON SIZE: ",
                len(all_marathon_data[0]),
                "and ",
                len(all_marathon_data[1]),
            )
            print(f"FINISHED YEAR {marathon.year}")

        return all_marathon_data

    def _get_num_of_pages(self, num_athletes: int) -> int:
        return math.ceil(num_athletes / 1000)

    def _get_athletes_and_results(
        self, marathon: MarathonEvent, gender: str, num_pages: int, sample: bool = False
    ) -> list[tuple[Athlete, MarathonEvent]]:

        athletes = []
        results = []
        for idx in range(1, num_pages + 1):
            sleep(randint(1,3))
            parser = self.get_parser(marathon, gender=gender, page=idx, sample=sample)
            parsers = parser.findAll(
                "li",
                attrs={
                    "class": ["list-group-item row", "list-active list-group-item row"]
                },
            )

            for parser in parsers:
                name = parser.find(
                    "h4", attrs={"class": "list-field type-fullname"}
                ).text  # name
                place_overall = parser.find(
                    "div",
                    attrs={
                        "class": "list-field type-place place-secondary hidden-xs numeric"
                    },
                ).text  # place overall
                place_gender = parser.find(
                    "div",
                    attrs={"class": "list-field type-place place-primary numeric"},
                ).text  # place gender
                time = parser.find("div", attrs={"class": "list-field type-time"}).text[
                    6:
                ]  # time
                bib = parser.find("div", attrs={"class": "list-field type-field"}).text[
                    3:
                ]  # bib
                age_group = parser.find(
                    "div", attrs={"class": "list-field type-age_class"}
                ).text[
                    8:
                ]  # age group
                first_and_last_name = name.split(', ')
                last_name = first_and_last_name[0]
                last_name_and_country = first_and_last_name[1].split(' (')
                print(last_name_and_country)
                first_name = last_name_and_country[0]
                if len(last_name_and_country) > 1:
                    country = last_name_and_country[1][:-1]
                else:
                    country=None
                
                
                athlete = Athlete(
                    first_name=first_name,
                    last_name=last_name,
                    country=country,
                    gender=SEX.MALE.value if gender == "M" else SEX.FEMALE.value,
                )
                marathon.athletes.append(athlete)
                athletes.append(athlete)
                time_obj = datetime.datetime.strptime(time, '%H:%M:%S')
                results.append(
                    Result(
                        place_overall=place_overall,
                        place_gender=place_gender,
                        finish_time=time_obj,
                        bib=bib,
                        age_group=age_group,
                        athlete_id=athlete.id,
                        marathon_event_id=marathon.id,
                    )
                )

            if sample:
                print("Returned early")
                return list(zip(athletes, results))

        return list(zip(athletes, results))
