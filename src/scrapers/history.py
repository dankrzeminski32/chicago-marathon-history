"""
Module used to scrape the official chicago marathon results website. Will be used via a command line "flask run seed"
"""
from bs4 import BeautifulSoup
import requests
from src.models.marathon import MarathonEvent

class EventJsonParser:
    """Parses json request to get unique event ids for history scraper"""
    URL = "https://chicago-history.r.mikatiming.com/2011/index.php?content=ajax2&func=getSearchFields&options[b][lists][event_main_group]=2015&options[b][lists][event]=&options[b][lists][sex]=&options[lang]=EN_CAP&options[pid]=start"
    content = requests.get(URL).json()

    def _get_event_list(self) -> list[dict]:
        """returns raw list of events in json format

        Returns:
            list[dict]: Multiple dictionaries with year and various event (marathon,wheelchair, handcycle) info,
        """
        return self.content['branches']['search']['fields']['event']['data']

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
        for idx in range(0, len(marathon_list)-1):
            if idx % 2 != 0:
                continue #skips current iteration
            year = marathon_list[idx]['v'][0][-4:]
            marathon_id = marathon_list[idx+1]['v'][0]
            parsed_marathon_events[int(year)] = MarathonEvent(int(year),marathon_id)
        return parsed_marathon_events


class HistoryScraper:
    """Scrapes Athlete data and finish times over 20 years"""
    def __init__(self):
        self.marathons: dict[int:MarathonEvent] = EventJsonParser().get_marathon_event_ids()

    def get_parser(self, year:int, *, gender:str=None):
        if gender is None:
            URL = f"https://chicago-history.r.mikatiming.com/2015/?page=1&event=ALL_EVENT_GROUP_{str(year)}&lang=EN_CAP&pid=search&pidp=start" 
        elif gender=='M' or gender=='W':
           URL = f"https://chicago-history.r.mikatiming.com/2015/?page=2&event={self.marathons[year].web_id}&lang=EN_CAP&pid=list&pidp=start&search%5Bsex%5D={gender}&search%5Bage_class%5D=%25"
        else:
            raise ValueError("Gender must be either 'M' or 'W'")

        content = requests.get(URL).content
        return BeautifulSoup(content, 'html.parser') # If this line causes an error, run 'pip install html5lib' or install html5lib

    def _populate_num_athletes(self) -> None:
        """populates marathon objects number of athletes for a given years"""
        for key in self.marathons:
            parser: BeautifulSoup = self.get_parser(key)
            marathon: MarathonEvent = self.marathons[key]
            total_participants = parser.find('li', attrs={'class': 'list-group-item'}).text.split()[0]
            marathon.num_athletes = int(total_participants)

    def _populate_num_female_athletes(self) -> None:
        """populates marathon objects number of female athletes for a given year"""
        for key in self.marathons:
            parser: BeautifulSoup = self.get_parser(key, gender="W")
            marathon: MarathonEvent = self.marathons[key]
            total_female_participants = parser.find('li', attrs={'class': 'list-group-item'}).text.split()[0]
            marathon.num_athletes_female = int(total_female_participants)

    def _populate_num_male_athletes(self) -> None:
        """populates marathon objects number of male athletes for a given year"""
        for key in self.marathons:
            parser: BeautifulSoup = self.get_parser(key, gender="M")
            marathon: MarathonEvent = self.marathons[key]
            total_male_participants = parser.find('li', attrs={'class': 'list-group-item'}).text.split()[0]
            marathon.num_athletes_male = int(total_male_participants)

    def getMarathons(self) -> dict[int:MarathonEvent]:
        """returns a list of MarathonEvent objects"""
        self._populate_num_athletes()
        self._populate_num_female_athletes()
        self._populate_num_male_athletes()
        return self.marathons