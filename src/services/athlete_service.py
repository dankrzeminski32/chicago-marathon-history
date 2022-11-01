
from ..models.athlete import Athlete

class AthleteService(object):
    
    def get():
        qry= Athlete.query.filter(Athlete.id==1)
        athlete = qry.first()
        print(athlete.results[0].finish_time)