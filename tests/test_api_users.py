import allure

from files import USERS_FILE_PATH, UPDATE_USER_FILE_PATH
from file_helpers.csv_helper import read_lines_from_csv
import pytest
from petstore_models import UserModel

@allure.title("Создание пользователя")
@pytest.mark.parametrize("data", read_lines_from_csv(USERS_FILE_PATH))
def test_create_user(api_client, data):
    response = api_client.create_user(data=dict(data))
    assert response.status_code == 200

@allure.title("Получение данных о пользователе по username")
def test_get_user_by_user_name(api_client, user_creation, user_deleting):
    response = api_client.get_user_by_username(username="i")
    assert response.status_code == 200
    json_response = response.json()
    UserModel.model_validate(json_response)

@allure.title("Удаление пользователя")
def test_delete_user(api_client, user_creation):
    response = api_client.delete_user(username="i")
    assert response.status_code == 200
    checking_delete = api_client.get_user_by_username(username="i")
    assert checking_delete.status_code == 404

@allure.title("Обновление данных пользователя")
@pytest.mark.parametrize("data", read_lines_from_csv(UPDATE_USER_FILE_PATH))
def test_update_user(api_client, user_creation,user_deleting, data):
    response = api_client.update_user(username="i", params=dict(data))
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["message"] == dict(data)["id"]