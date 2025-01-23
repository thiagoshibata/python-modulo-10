from datetime import datetime
from src.models.repository.interfaces.orders_repository import OrdersRepositoryInterface
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.validators.registry_order_validator import registry_order_validator


class RegistryOrder:
    def __init__(self, order_repository: OrdersRepositoryInterface) -> None:
        self.__order_repository = order_repository

    def registry(self, http_request: HttpRequest) -> HttpResponse:
        try:
            body = http_request.body
            self.__validate_body(body)

            new_order = self.__format_new_order(body)
            self.__registry_order(new_order)

            return self.__formated_response()

        except Exception as exception:
            return HttpResponse(
                body = { "error": str(exception)},
                status_code=400
            )

    def __validate_body(self, body: dict) -> None:
        registry_order_validator(body)

    def __format_new_order(self, body: dict) -> dict:
        '''Adding 'created_at' in new order'''
        new_order = body["data"]
        new_order = {**new_order, "created_at": datetime.now()}
        return new_order

    def __registry_order(self, new_order: dict) -> None:
        '''Inserting document on database'''
        self.__order_repository.insert_document(new_order)

    def __formated_response(self) -> dict:
        '''Formating response to routes'''
        return HttpResponse(
            body={
                "data": {
                    "type": "Order",
                    "count": 1,
                    "registry": True
                }
            },
            status_code=201
        )
