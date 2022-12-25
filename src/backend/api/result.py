from flask import Blueprint, jsonify
from src.backend.models.result import ResultSchema
from src.backend.services.result_service import ResultService, InvalidSexInput
from src.backend.constants import ENDPOINTS, ERROR_MESSAGES

result_api_bp = Blueprint("result_api", __name__, url_prefix=ENDPOINTS.RESULTS.value)

@result_api_bp.route("/<int:year>", methods=["GET"])
def get_results_by_year(year):
    schema = ResultSchema(many=True)
    all_results = ResultService.get_all_by_year(year)
    if all_results is None:
        return jsonify({"Error": ERROR_MESSAGES.INVALID_YEAR.value})
    results = schema.dump(all_results)
    return jsonify(results)

@result_api_bp.route("/<int:year>/<string:sex>/<int:limit>", methods=["GET"])
@result_api_bp.route("/<int:year>/<string:sex>", defaults={'limit': None} ,methods=["GET"])
def get_results_by_year_and_sex(year, sex, limit):
    schema = ResultSchema(many=True)
    try:
        all_results = ResultService.get_all_by_year(year, sex, limit)
    except InvalidSexInput:
        return jsonify({"Error": ERROR_MESSAGES.INVALID_SEX_INPUT.value})
    if all_results is None:
        return jsonify({"Error": ERROR_MESSAGES.INVALID_YEAR.value})
    results = schema.dump(all_results)
    return jsonify(results)