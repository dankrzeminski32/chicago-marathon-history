from flask import Blueprint
from src.models.athlete import AthleteSchema
from flask import jsonify
from src.services.athlete_service import AthleteService
from src.constants import ENDPOINTS

athlete_api_bp = Blueprint('athlete_api',__name__, url_prefix=ENDPOINTS.ATHLETES.value)

@athlete_api_bp.route('/',methods=['GET'])
def get_athletes():
        schema = AthleteSchema(many=True)
        all_athletes = AthleteService.get_all()
        athletes = schema.dump(all_athletes)
        return jsonify(athletes)

@athlete_api_bp.route('/<year>',methods=['GET'])
def get_athletes_by_year(year):
        schema = AthleteSchema(many=True)
        all_athletes = AthleteService.get_all_by_year(year)
        athletes = schema.dump(all_athletes)
        return jsonify(athletes)
