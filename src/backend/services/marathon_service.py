from src.backend.models.marathon import MarathonEvent
from sqlalchemy.exc import NoResultFound

class MarathonEventService(object):
    """Class used to execute queries and retrieve data related to MarathonEvent objects"""

    @staticmethod
    def get_all() -> list[MarathonEvent]:
        """Get a list of all the Marathon Events"""
        return MarathonEvent.query.all()

    @staticmethod
    def get_by_year(year: int) -> MarathonEvent | None:
        """Gets a single MarathonEvent for a given year"""
        try:
            marathon = MarathonEvent.query.filter_by(year=year).one()
            return marathon
        except NoResultFound:
            return None
