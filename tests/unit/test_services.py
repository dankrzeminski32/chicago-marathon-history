from src.services.athlete_service import AthleteService
from src.services.marathon_service import MarathonEventService

def test_AthleteService_get_all(app):
    """
    GIVEN an AthleteService class
    WHEN get_all is called
    THEN return 25 marathon events
    """
    marathons = AthleteService.get_all()
    assert len(marathons) == 25
