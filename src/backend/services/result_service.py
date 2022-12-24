from src.backend.models.result import Result
from src.backend.services.marathon_service import MarathonEventService
from src.backend.constants import SEX


class ResultService(object):
    """Class used to execute queries and retrieve data related to Result objects"""

    @staticmethod
    def get_all() -> list[Result]:
        """Gets a list of all results in our db"""
        return Result.query.all()

    @staticmethod
    def get_all_by_year(year: int, sex: str = None) -> list[Result] | None:
        """Gets a list of results by year and optional sex filter """
        marathon = MarathonEventService.get_by_year(year)
        if marathon and not sex:
            return marathon.results
        elif marathon and sex:
            if sex=='M':
                return [result for result in marathon.results if result.athlete.gender == SEX.MALE.value]
            elif sex=='F':
                return [result for result in marathon.results if result.athlete.gender == SEX.FEMALE.value]
            else:
                raise InvalidSexInput 
        else:
            return None

class InvalidSexInput(Exception):
    """ Raised when sex input is not 'M' or 'F' """
    pass