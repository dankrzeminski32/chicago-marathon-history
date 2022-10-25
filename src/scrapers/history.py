from dataclasses import dataclass
from bs4 import BeautifulSoup
import requests


# table = soup.find('ul', attrs = {'class':'list-group list-group-multicolumn'}) 

# for row in table.findAll('li', attrs = {'class':"list-active list-group-item row"}):
#     for name in row.find('h4', attrs = {"type-fullname"}):
#         print(name.text)

class HistoryScraper:
    """Scrapes Athlete data and finish times over 20 years"""
    URL = "https://chicago-history.r.mikatiming.com/2015/?page=1&event=MAR_999999107FA31100000000C9&lang=EN_CAP&num_results=100&pid=list&search%5Bsex%5D=M&search%5Bage_class%5D=%25"
    content = requests.get(URL).content
    soup = BeautifulSoup(content, 'html.parser') # If this line causes an error, run 'pip install html5lib' or install html5lib

    def get_num_athletes(self):
        race_info = self.soup.find('li', attrs={'class': 'list-group-item'})
        return race_info

@dataclass
class MarathonEvent:
    year: int
    id: str

class EventJsonParser:
    """Parses json request to get unique event ids for history scraper"""
    URL = "https://chicago-history.r.mikatiming.com/2011/index.php?content=ajax2&func=getSearchFields&options[b][lists][event_main_group]=2015&options[b][lists][event]=&options[b][lists][sex]=&options[lang]=EN_CAP&options[pid]=start"
    content = requests.get(URL).json()

    def get_event_list(self) -> list[dict]:
        """returns raw list of events in json format

        Returns:
            list[dict]: Multiple dictionaries with year and various event (marathon,wheelchair, handcycle) info,
        """
        return self.content['branches']['search']['fields']['event']['data']

    def get_marathon_data(self) -> list[dict]:
        """returns raw list of marathon id's and marathon year information

        Returns:
            list[dict]: multiple dictionaries containing year and marathon id information
        """
        all_events = self.get_event_list()
        marathon_list = [v for i, v in enumerate(all_events) if i % 4 < 2]            
        return marathon_list

    def get_parsed_marathon_events(self) -> list[MarathonEvent]:
        """parses json data and returns a user friendly list of MarathonEvent objects

        Returns:
            list[MarathonEvent]: list of MarathonEvent objects
        """
        marathon_list = self.get_marathon_data()
        parsed_marathon_events: list[MarathonEvent] = []
        for idx in range(0, len(marathon_list)-1):
            if idx % 2 != 0:
                continue #skips current iteration
            year = marathon_list[idx]['v'][0][-4:]
            marathon_id = marathon_list[idx+1]['v'][0]
            parsed_marathon_events.append(MarathonEvent(year, marathon_id))
        return parsed_marathon_events
