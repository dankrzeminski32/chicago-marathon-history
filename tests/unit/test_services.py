from src.services.athlete_service import AthleteService
from src.services.marathon_service import MarathonEventService
import pytest

### ATHLETE SERVICE TESTS ###
def test_AthleteService_get_all(test_client):
    """
    GIVEN an AthleteService class
    WHEN get_all is called
    THEN return 1250 athletes (sample)
    """
    athletes = AthleteService.get_all()
    assert len(athletes) == 1250


### MARATHON SERVICE TESTS ###
def test_MarathonService_get_all(test_client):
    """
    GIVEN an MarathonService class
    WHEN get_all is called
    THEN return 25 MarathonEvents (sample)
    """
    marathons = MarathonEventService.get_all()
    assert len(marathons) == 25

@pytest.mark.parametrize("year, output", [(2018,2018),(2017, 2017),(2032,None),(1995, None)])
def test_MarathonService_get_by_year(test_client, year, output):
    """
    GIVEN a MarathonService class
    WHEN get_by_year() is called with a valid parameter
    THEN return the given MarathonEvent object
    """
    marathon = MarathonEventService.get_by_year(year) 
    if year <= 2022 and year >= 1996:
        assert marathon.year == output
    else:
        assert marathon == output