
from ..models.athlete import Athlete

class AthleteService(object):
    """Class used to execute queries and retrieve data related to MarathonEvent objects"""
    
    @staticmethod
    def get_all() -> list[Athlete]:
        """Gets a list of all Athletes in our db"""
        return Athlete.query.all()
