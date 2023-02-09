from src.models.athlete import Athlete
from src.services.marathon_service import MarathonEventService


class AthleteService(object):
    """Class used to execute queries and retrieve data related to MarathonEvent objects"""

    @staticmethod
    def get_all() -> list[Athlete]:
        """Gets a list of all Athletes in our db"""
        return Athlete.query.all()

    @staticmethod
    def get_all_by_year(year: int) -> list[Athlete] | None:
        """Gets a list of all athletes for a given year"""
        marathon = MarathonEventService.get_by_year(year)
        if marathon:
            return marathon.athletes
        else:
            return None
