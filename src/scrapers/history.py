from bs4 import BeautifulSoup
import requests


# table = soup.find('ul', attrs = {'class':'list-group list-group-multicolumn'}) 

# for row in table.findAll('li', attrs = {'class':"list-active list-group-item row"}):
#     for name in row.find('h4', attrs = {"type-fullname"}):
#         print(name.text)

class HistoryScraper:
    """Scrapes Athlete data and finish times over 40 years"""
    # UURL = "https://chicago-history.r.mikatiming.com/2019/?page=1&event=MAR_999999107FA31100000000C9&lang=EN_CAP&num_results=100&pid=list&search%5Bsex%5D=M&search%5Bage_class%5D=%25"
    URL = "https://chicago-history.r.mikatiming.com/2015/?page=1&event=MAR_999999107FA31100000000C9&lang=EN_CAP&num_results=100&pid=list&search%5Bsex%5D=M&search%5Bage_class%5D=%25"
    content = requests.get(URL).content
    soup = BeautifulSoup(content, 'html.parser') # If this line causes an error, run 'pip install html5lib' or install html5lib

    def get_num_athletes(self):
        race_info = self.soup.find('li', attrs={'class': 'list-group-item'})
        return race_info

class EventJsonParser:
    """Parses json request to get unique event ids for history scraper"""
    URL = "https://chicago-history.r.mikatiming.com/2011/index.php?content=ajax2&func=getSearchFields&options[b][lists][event_main_group]=2015&options[b][lists][event]=&options[b][lists][sex]=&options[lang]=EN_CAP&options[pid]=start"
    content = requests.get(URL).json()
    event_data: list[int] = content['branches']['search']['fields']['event']['data'][0]

    def getJson(self):
        return self.content['branches']['search']['fields']['event']['data'][0]

print(EventJsonParser().getJson())