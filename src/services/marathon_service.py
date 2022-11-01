from ..models.marathon import MarathonEvent

from .. import db

class MarathonEventService(object):
    """Class used to execute queries and retrieve data related to MarathonEvent objects"""
    @staticmethod
    def get_list() -> list[MarathonEvent]:
        """Get a list of all the Marathon Events"""
        return MarathonEvent.query.all()

    @staticmethod
    def count() -> int:
        """Count how many Marathons are in the system."""
        return MarathonEvent.query.count()

    @staticmethod
    def get_MarathonEvent(year) -> MarathonEvent | None:
        """Get the user for this code"""
        marathon = MarathonEvent.query.filter(MarathonEvent.year == year)

        if res is not None:
            return res.user
        else:
            return None
