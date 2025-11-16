import pytest

from clients.operations_client import OperationsClient, get_operations_client
from config import Settings
from schema.operations import OperationsSchema


@pytest.fixture
def operations_client(settings: Settings) -> OperationsClient:
    return get_operations_client(settings)


@pytest.fixture
def function_operation(operations_client: OperationsClient) -> OperationsSchema:
    operation = operations_client.create_operation()
    yield operation

    operations_client.delete_operation_api(operation.id)
