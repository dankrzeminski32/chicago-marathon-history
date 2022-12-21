from src.backend.models.result import Result
from src.backend.services.marathon_service import MarathonEventService


class ResultService(object):
    """Class used to execute queries and retrieve data related to Result objects"""

    @staticmethod
    def get_all() -> list[Result]:
        """Gets a list of all Athletes in our db"""
        return Result.query.all()

    @staticmethod
    def get_all_by_year(year: int) -> list[Result] | None:
        marathon = MarathonEventService.get_by_year(year)
        if marathon:
            return marathon.results
        else:
            return None
