import allure
import pytest
from files import ORDER_FILE_PATH
from file_helpers.csv_helper import read_lines_from_csv
from petstore_models import OrderModel

@allure.title("Получение количества питомцев с перечислением по статусам")
def test_get_pet_inventory(api_client):
    response = api_client.get_pet_inventory()
    assert response.status_code == 200
    json_response = response.json()
    assert json_response

@allure.title("Заявка на получение питомца")
@pytest.mark.parametrize("data", read_lines_from_csv(ORDER_FILE_PATH))
def test_order_pet(api_client, pet_creation, pet_deleting, data):
    response = api_client.order_pet(data=dict(data))
    assert response.status_code == 200
    json_response = response.json()
    OrderModel.model_validate(json_response)
