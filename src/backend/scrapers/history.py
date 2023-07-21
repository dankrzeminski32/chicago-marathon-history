"""
Module used to scrape the official chicago marathon results website. Will be used via a command line "flask run seed"
"""
import requests
from src.backend.models.marathon import MarathonEvent
from src.backend.models.athlete import Athlete
from src.backend.models.result import Result
from src.backend.services.marathon_service import MarathonEventService
from src.backend.constants import SEX
import datetime
import asyncio
import aiohttp
from src.backend.models.marathon import MarathonDataHTML
from multiprocessing import Pool
import sys
from time import time


sys.setrecursionlimit(25000)


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
        marathon_list = []
        for event in all_events:
            if event["v"][1].startswith("All") or event["v"][1] == "Marathon":
                marathon_list.append(event)

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


class MarathonParticipantCountScraper:
    """Scrapes total number of participants for each marathon"""

    def __init__(self):
        self.marathons: dict[
            int:MarathonEvent
        ] = EventJsonParser().get_marathon_event_ids()

    def _fetch_html(self) -> list[MarathonDataHTML]:
        htmls = []
        for marathon in self.marathons.values():
            htmls.append(marathon.get_male_and_female_results())
        return htmls

    def _populate_marathon_with_participant_data(
        self, parsers: [str, MarathonDataHTML]
    ) -> None:
        parsers["M"][0].marathon = parsers["W"][0].marathon
        parsers["M"][0].marathon.num_athletes_male = self._find_total_participants(
            parsers["M"][0]
        )
        parsers["W"][0].marathon.num_athletes_female = self._find_total_participants(
            parsers["W"][0]
        )
        return parsers["M"][0].marathon

    def _find_total_participants(self, html_data: MarathonDataHTML) -> int:
        total_participants = html_data.find(
            "li", attrs={"class": "list-group-item"}
        ).text.split()[0]
        return int(total_participants)

    def get_marathons(self) -> list[MarathonEvent]:
        """returns a list of MarathonEvent objects"""
        parsers = self._fetch_html()
        with Pool(20) as p:
            data = p.map(self._populate_marathon_with_participant_data, parsers)
        return data


class AthleteResultScraper:
    """Scrapes Athletes and Results for each marathon"""

    def __init__(self):
        self.marathons: list[MarathonEvent] = MarathonEventService.get_all()

    def fetch_html(self) -> list[MarathonDataHTML]:
        htmls = []
        for marathon in self.marathons:
            male_results = marathon.get_male_results_html()
            female_results = marathon.get_female_results_html()
            htmls.append(male_results)
            htmls.append(female_results)
            print(f"Finished Getting HTML for {marathon.year}")
            print(f"Total Number of HTML Documents - {len(male_results)+len(female_results)}")
        return htmls

    def parse_for_athletes_and_results(self):
        parsers = self.fetch_html()
        parsers = [item for sublist in parsers for item in sublist] #Flatten the list
        with Pool(20) as p:
            data = p.map(self._parse_raw_html, parsers)

        return data

    def _parse_raw_html(self, parser: MarathonDataHTML) -> tuple[Athlete | Result]:
        print(type(parser))
        athletes = []
        results = []
        all_rows = parser.findAll(
            "li",
            attrs={"class": ["list-group-item row", "list-active list-group-item row"]},
        )

        for row in all_rows:
            athlete = self._get_athlete_info_from_row(row)
            if athlete:
                athlete.gender = (
                    SEX.MALE.value if parser.gender == "M" else SEX.FEMALE.value
                )
                result = self._get_result_info_from_row(row)
                result.athlete = athlete
                result.marathon_event_id = parser.marathon_id
                athletes.append(athlete)
                results.append(result)

        print(f"Finished Parsing HTML for {parser.marathon.year}")
        print(f"Total Athletes Found: {len(athletes)}")
        print(f"Total Results Found: {len(results)}")
        return list(zip(athletes, results))

    def _get_athlete_info_from_row(self, row):
        try:
            name = row.find("h4", attrs={"class": "list-field type-fullname"}).text  # name
            first_and_last_name = name.split(", ")
            last_name = first_and_last_name[0]
            last_name_and_country = first_and_last_name[1].split(" (")
            first_name = last_name_and_country[0]
            if len(last_name_and_country) > 1:
                country = last_name_and_country[1][:-1]
            else:
                country = None
            return Athlete(
                first_name=first_name,
                last_name=last_name,
                country=country,
            )
        except IndexError:
            print("ENCOUNTERED INDEX ERROR")

    def _get_result_info_from_row(self, row):
        place_overall = row.find(
            "div",
            attrs={"class": "list-field type-place place-secondary hidden-xs numeric"},
        ).text  # place overall
        place_gender = row.find(
            "div",
            attrs={"class": "list-field type-place place-primary numeric"},
        ).text  # place gender
        time = row.find("div", attrs={"class": "list-field type-time"}).text[6:]  # time
        bib = row.find("div", attrs={"class": "list-field type-field"}).text[3:]  # bib
        age_group = row.find("div", attrs={"class": "list-field type-age_class"}).text[
            8:
        ]  # age group
        time_obj = datetime.datetime.strptime(time, "%H:%M:%S")

        return Result(
            place_overall=place_overall,
            place_gender=place_gender,
            finish_time=time_obj,
            bib=bib,
            age_group=age_group,
        )
