from flask import Blueprint, jsonify
from src.backend.models.result import ResultSchema
from src.backend.services.result_service import ResultService
from src.backend.constants import ENDPOINTS, ERROR_MESSAGES

result_api_bp = Blueprint("result_api", __name__, url_prefix=ENDPOINTS.RESULTS.value)

@result_api_bp.route("/<year>", methods=["GET"])
def get_results_by_year(year):
    schema = ResultSchema(many=True)
    all_results = ResultService.get_all_by_year(year)
    if all_results is None:
        return jsonify({"Error": ERROR_MESSAGES.INVALID_YEAR.value})
    results = schema.dump(all_results)
    return jsonify(results)
