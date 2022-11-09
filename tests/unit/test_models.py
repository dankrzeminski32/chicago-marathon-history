from src.models.marathon import MarathonEvent
from src.models.athlete import Athlete
from src.constants import SEX

def test_new_marathon():
    """
    GIVEN a MarathonEvent model
    WHEN a new MarathonEvent is created
    THEN check the year, web_id, num_athletes, num_athletes_female, num_athletes_male are defined correctly
    """
    marathon = MarathonEvent(2021, "xyz")
    assert marathon.year == 2021
    assert marathon.web_id == "xyz"
    assert marathon.num_athletes == None
    assert marathon.num_athletes_female == None
    assert marathon.num_athletes_male == None

    
def test_new_athlete():
    """
    GIVEN a Athlete model
    WHEN a new Athlete is created
    THEN check to make sure the relationship back to marathons is working properly
    """
    athlete = Athlete(name="dan", gender=SEX.MALE.value)
    assert athlete.name == "dan"
    assert athlete.gender == 1