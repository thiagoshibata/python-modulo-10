from bson.objectid import ObjectId
from .interfaces.orders_repository import OrdersRepositoryInterface

class OrdersRepository(OrdersRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__collection_name = "orders"
        self.__db_connection = db_connection

    def insert_document(self, document: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)

    def insert_list_of_documents(self, list_of_documents: list) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)

    def select_many(self, doc_filter: dict) -> list:
        """ select multiple documents according to the filter """
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(doc_filter)
        return data

    def select_one(self, doc_filter: dict) -> dict:
        """ select the first element found """
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(doc_filter)
        return response

    def select_many_with_properties(self, doc_filter: dict) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            doc_filter, # search filter
            { "_id": 0, "cupom": 0 } # Return options | removing properties of the return
        )
        return data

    def select_if_property_exists(self) -> dict:
        """select elements if properties exists"""
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find(
            {"address": {"$exists": True}}, # Only exists field
            { "_id": 0, "cupom":0 } # removing properties of the return
        )
        return response

    def select_by_object_id(self, object_id: str) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one({"_id" : ObjectId(object_id)})
        return data

    def edit_registry(self, order_id: str, update_fields: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            { "_id" : ObjectId(order_id)}, #Filters
            { "$set": update_fields } #Edit data
        )

    def edit_many_registries(self, edit_data: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_many(
            { "itens.refrigerante": { "$exists": True } }, #Filters
            { "$set": edit_data } #Edit data
        )
    def edit_registry_with_increment(self, object_id: str, edit_data: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            { "_id" : ObjectId(object_id)}, #Filters
            { "$inc": edit_data } #Edit data with increment. For decrement use negative number
        )

    def delete_registry(self, object_id: str) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_one(
            {"_id": ObjectId(object_id)}
        )
    def delete_many_registries(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_many(
            {"itens.refrigerante": {"$exists":True}}
        )
