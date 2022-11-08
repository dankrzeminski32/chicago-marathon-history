from ..models.marathon import MarathonEvent

from .. import db

class MarathonEventService(object):
    """Class used to execute queries and retrieve data related to MarathonEvent objects"""
    
    @staticmethod
    def get_all() -> list[MarathonEvent]:
        """Get a list of all the Marathon Events"""
        return MarathonEvent.query.all()
