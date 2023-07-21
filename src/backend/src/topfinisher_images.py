import wikipedia
from src.services.marathon_service import MarathonEventService
from src.services.result_service import ResultService
import bs4 as bs
import urllib.request
from src.models.athlete import Athlete
from wikipedia.exceptions import DisambiguationError
from src import db


class TopFinisherImageRetriever:
    def get_images():
        marathon_service = MarathonEventService()
        result_service = ResultService()
        all_marathons = marathon_service.get_all()

        for marathon in all_marathons:
            top3results = result_service.get_all_by_year(year=marathon.year, limit=3)
            for result in top3results:
                athlete_name = result.athlete.first_name + " " + result.athlete.last_name
                # WIKIPEDIA SEARCH
                page_suggestion = wikipedia.search(athlete_name)
                if len(page_suggestion) > 0:
                    try:
                        athlete_page = wikipedia.page(page_suggestion[0], auto_suggest=False)
                        TopFinisherImageRetriever.parse_html(athlete_page.url, result.athlete)
                    except DisambiguationError:
                        pass
                
    def parse_html(athlete_link: str, athlete: Athlete):
        source = urllib.request.urlopen(athlete_link).read()
        soup = bs.BeautifulSoup(source,'html')
        img_element = soup.find("td", class_="infobox-image")
        if img_element is not None:
            img_element = img_element.find("img")['src']
            img_link = img_element[2:]
            athlete.img = img_link
            db.session.commit()
            
