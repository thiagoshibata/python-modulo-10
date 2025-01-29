from src.models.repository.interfaces.orders_repository import OrdersRepositoryInterface
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.errors.types.http_not_found import HttpNotFoundError
from src.errors.error_handler import error_handler

class RegistryFinder:
    def __init__(self, order_repository: OrdersRepositoryInterface) -> None:
        self.__order_repository = order_repository

    def find(self, http_request: HttpRequest) -> HttpResponse:
        try:
            order_id = http_request.params["order_id"]
            order = self.__search_order(order_id)
            return self.__format_response(order)

        except Exception as exception:
            return error_handler(exception)

    def __search_order(self, order_id: str) -> dict:
        order = self.__order_repository.select_by_object_id(order_id)
        if not order: raise HttpNotFoundError("Order not found")
        return order

    def __format_response(self, order: dict) -> HttpResponse:
        order["_id"] = str(order["_id"])
        return HttpResponse(
            body={
                "data":{
                    "count": 1,
                    "type": "Order",
                    "attributes": order
                }
            },
            status_code=200
        )
