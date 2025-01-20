import pytest
from src.models.connection.connection_handler import DBConnectionHandler
from src.models.repository.orders_repository import OrdersRepository

db_connection_handler = DBConnectionHandler()
db_connection_handler.connect_to_db()
conn = db_connection_handler.get_db_connection()

@pytest.mark.skip(reason="interacao com o banco de dados")
def test_insert_document():
    orders_repository = OrdersRepository(conn)
    my_doc = { "alguma": "coisa" , "valor": 5}
    orders_repository.insert_document(my_doc)

@pytest.mark.skip(reason="interacao com o banco de dados")
def test_insert_list_of_documents():
    orders_repository = OrdersRepository(conn)
    my_docs = [{ "elem1": "coisa1"}, {"elem2":"coisa2"}, {"elem3":"coisa3"}]
    orders_repository.insert_list_of_documents(my_docs)

@pytest.mark.skip(reason="interacao com o banco de dados")
def test_select_many():
    orders_repository = OrdersRepository(conn)
    doc_filter = { "cupom" : False }
    response = orders_repository.select_many(doc_filter)
    print()
    for doc in response:
        print(doc)
        print(doc["itens"])
        print()

@pytest.mark.skip(reason="interacao com o banco de dados")
def test_select_one():
    orders_repository = OrdersRepository(conn)
    doc_filter = { "client" : "Thiago" }
    response = orders_repository.select_one(doc_filter)
    print()
    print(response)

@pytest.mark.skip(reason="interacao com o banco de dados")
def test_select_many_with_properties():
    orders_repository = OrdersRepository(conn)
    doc_filter = { "cupom" : True }
    response = orders_repository.select_many_with_properties(doc_filter)
    print()
    for doc in response:
        print(doc)
        print()

@pytest.mark.skip(reason="interacao com o banco de dados")
def test_select_if_property_exists():
    orders_repository = OrdersRepository(conn)
    response = orders_repository.select_if_property_exists()
    print()
    for doc in response:
        print(doc)
        print()

@pytest.mark.skip(reason="interacao com o banco de dados")
def test_select_many_with_multiple_filters():
    """Similar to the “AND” search in SQL"""
    orders_repository = OrdersRepository(conn)
    doc_filter = { "cupom" : True,
                  "itens.doce": {"$exists": True}
                  }
    response = orders_repository.select_many(doc_filter)
    print()
    for doc in response:
        print(doc)
        print()

@pytest.mark.skip(reason="interacao com o banco de dados")
def test_select_many_with_or_filter():
    """Similar to the "OR" search in SQL"""
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "$or":[
            {"address":{"$exists": True}},
            {"itens.doce.tipo": "chocolate"}
        ]
    }
    response = orders_repository.select_many(doc_filter)
    print()
    for doc in response:
        print(doc)
        print()

@pytest.mark.skip(reason="interacao com o banco de dados")
def test_select_by_object_id():
    orders_repository = OrdersRepository(conn)
    object_id = "6784fb2afac3010aef8f106f"
    response = orders_repository.select_by_object_id(object_id)
    print()
    print(response)

@pytest.mark.skip(reason="interacao com o banco de dados")
def test_edit_registry():
    orders_repository = OrdersRepository(conn)
    object_id = "6784fb2afac3010aef8f106f"
    edit_data = {"itens.pizza.quantidade" : 30 }
    orders_repository.edit_registry(object_id, edit_data)

@pytest.mark.skip(reason="interacao com o banco de dados")
def test_edit_many_registries():
    orders_repository = OrdersRepository(conn)
    edit_data = { "itens.refrigerante.quantidade":100 }
    orders_repository.edit_many_registries( edit_data)

@pytest.mark.skip(reason="interacao com o banco de dados")
def test_edit_registry_with_increment():
    orders_repository = OrdersRepository(conn)
    object_id = "6784fb2afac3010aef8f106f"
    edit_data = {"itens.pizza.quantidade" : 30 }
    orders_repository.edit_registry_with_increment(object_id, edit_data)
