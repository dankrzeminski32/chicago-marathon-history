from flask import Blueprint, jsonify
from src.backend.services.marathon_service import MarathonEventService
from src.backend.models.marathon import MarathonSchema
from src.backend.constants import ENDPOINTS, ERROR_MESSAGES

marathon_api_bp = Blueprint(
    "marathon_api", __name__, url_prefix=ENDPOINTS.MARATHONS.value
)


@marathon_api_bp.route("/")
def get_marathons():
    schema = MarathonSchema(many=True)
    all_marathons = MarathonEventService.get_all()
    marathons = schema.dump(all_marathons)
    return jsonify(marathons)


@marathon_api_bp.route("/<year>")
def get_marathon_by_year(year):
    schema = MarathonSchema()
    marathon = MarathonEventService.get_by_year(year)
    if marathon is None:
        return jsonify({"Error": ERROR_MESSAGES.INVALID_YEAR.value})
    marathons = schema.dump(marathon)
    return jsonify(marathons)
