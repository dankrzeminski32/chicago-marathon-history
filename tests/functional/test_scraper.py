from src.scrapers import history

def test_get_marathons():
    """
    GIVEN a HistoryScraper object
    WHEN HistoryScraper runs getMarathons
    THEN return a valid marathonEvent with the correct data
    """
    scraper = history.HistoryMarathonScraper()
    test_dict = {2021: scraper.marathons[2021]}
    scraper.marathons = test_dict
    marathon_event_data = scraper.get_marathons()
    test_obj = marathon_event_data[2021]
    assert test_obj.year == 2021 
    assert test_obj.web_id == 'MAR_9TGG9638F1'
    assert test_obj.num_athletes == 33543
    assert test_obj.num_athletes_female == 11876
    assert test_obj.num_athletes_male == 14202

def test_get_marathon_event_ids():
    """
    GIVEN an EventJsonParser object
    WHEN asking for event ids
    THEN return a list full of all 25 marathon event ids
    """
    scraper = history.EventJsonParser()
    marathon_events: dict = scraper.get_marathon_event_ids()
    assert(len(marathon_events) == 25)