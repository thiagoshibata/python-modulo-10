from flask import Blueprint, jsonify, request
from src.main.http_types.http_request import HttpRequest

from src.main.composer.registry_order_composer import registry_order_composer
from src.main.composer.registry_finder_composer import registry_finder_composer
from src.main.composer.registry_updater_composer import registry_updater_composer

delivery_routes_bp = Blueprint("delivery_routes", __name__)

@delivery_routes_bp.route("/delivery/order", methods=["POST"])
def registry_order():
    use_case = registry_order_composer()
    http_request = HttpRequest(body=request.json)
    # Will send HttpResponse to logic
    response = use_case.registry(http_request)
    # The logic will return an HttpResponse

    return jsonify(response.body), response.status_code

@delivery_routes_bp.route("/delivery/order/<order_id>", methods=["GET"])
def registry_finder(order_id):
    use_case = registry_finder_composer()
    http_request = HttpRequest(params={"order_id": order_id})

    # The logic will return an HttpResponse
    response = use_case.find(http_request)

    return jsonify(response.body), response.status_code

@delivery_routes_bp.route("/delivery/order/<order_id>", methods=["PATCH"])
def registry_updater(order_id):
    use_case = registry_updater_composer()
    http_request = HttpRequest(
            params={"order_id": order_id},
            body=request.json
        )

    # The logic will return an HttpResponse
    response = use_case.update(http_request)

    return jsonify(response.body), response.status_code
