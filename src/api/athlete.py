from flask import Blueprint
from src.models.athlete import AthleteSchema
from flask import jsonify
from src.services.athlete_service import AthleteService

athlete_api_bp = Blueprint('athlete_api',__name__, url_prefix="/athletes")

@athlete_api_bp.route('')
def get_athletes():
        schema = AthleteSchema(many=True)
        all_athletes = AthleteService.get_all()
        athletes = schema.dump(all_athletes)
        return jsonify(athletes)

@a