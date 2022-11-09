from flask import Blueprint
from src.models.athlete import AthleteSchema
from flask import jsonify
from src.services.athlete_service import AthleteService
from src.constants import ENDPOINTS, ERROR_MESSAGES

athlete_api_bp = Blueprint("athlete_api", __name__, url_prefix=ENDPOINTS.ATHLETES.value)


@athlete_api_bp.route("/", methods=["GET"])
def get_athletes():
    schema = AthleteSchema(many=True)
    all_athletes = AthleteService.get_all()
    athletes = schema.dump(all_athletes)
    return jsonify(athletes)


@athlete_api_bp.route("/<year>", methods=["GET"])
def get_athletes_by_year(year):
    schema = AthleteSchema(many=True)
    all_athletes = AthleteService.get_all_by_year(year)
    if all_athletes is None:
        return jsonify({"Error": ERROR_MESSAGES.INVALID_YEAR.value})
    athletes = schema.dump(all_athletes)
    return jsonify(athletes)
