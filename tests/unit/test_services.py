from src.backend.services.athlete_service import AthleteService
from src.backend.services.marathon_service import MarathonEventService
from src.backend.services.result_service import ResultService
from src.backend.constants import SEX
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


def test_AthleteService_get_all_by_year(test_client):
    """
    Given an AthleteService class
    WHEN get_all_by_year is called with valid input
    return all athletes for a given year
    """
    athletes = AthleteService.get_all_by_year(2019)
    assert len(athletes) == 50
    bad_input_athletes = AthleteService.get_all_by_year(2050)
    assert bad_input_athletes == None


### MARATHON SERVICE TESTS ###
def test_MarathonService_get_all(test_client):
    """
    GIVEN an MarathonService class
    WHEN get_all is called
    THEN return 25 MarathonEvents (sample)
    """
    marathons = MarathonEventService.get_all()
    assert len(marathons) == 25


@pytest.mark.parametrize(
    "year, output", [(2018, 2018), (2017, 2017), (2032, None), (1995, None)]
)
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

### RESULT SERVICE TESTS ###
def test_ResultService_get_all(test_client):
    """
    GIVEN a ResultService class
    WHEN get_all is called
    THEN return 25 MarathonEvents (sample)
    """
    results = ResultService.get_all()
    assert len(results) == 1250


def test_ResultService_get_all_by_year(test_client):
    """
    GIVEN a MarathonService class
    WHEN get_by_year() is called with a valid parameter
    THEN return the given MarathonEvent object
    """
    results = ResultService.get_all_by_year(2019)
    assert len(results) == 50
    assert results[0].marathon_event.year == 2019

def test_ResultService_get_all_by_year_female(test_client):
    """
    GIVEN a MarathonService class
    WHEN get_by_year() is called with a valid parameter
    THEN return the given MarathonEvent object
    """
    results = ResultService.get_all_by_year(2019,'F')
    assert len(results) == 25
    assert results[0].athlete.gender == SEX.FEMALE.value
    assert results[0].marathon_event.year == 2019


def test_ResultService_get_all_by_year_male(test_client):
    """
    GIVEN a MarathonService class
    WHEN get_by_year() is called with a valid parameter
    THEN return the given MarathonEvent object
    """
    results = ResultService.get_all_by_year(2019,'M')
    assert len(results) == 25
    assert results[0].athlete.gender == SEX.MALE.value
    assert results[0].marathon_event.year == 2019