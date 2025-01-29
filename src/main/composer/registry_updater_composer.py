from src.use_cases.registry_updater import RegistryUpdater
from src.models.repository.orders_repository import OrdersRepository
from src.models.connection.connection_handler import db_connection_handler

def registry_updater_composer():
    conn = db_connection_handler.get_db_connection()
    model = OrdersRepository(conn)
    use_case = RegistryUpdater(model)

    return use_case
