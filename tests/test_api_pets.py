import allure
import pytest
from petstore_models import PetModel

INVALID_ID_VALUE = 9223372036854775809

@allure.title("Запрос списка питомцев с разными статусами")
@pytest.mark.parametrize(["status", "code"],
                         [("available", 200), ("pending", 200), ("sold", 200)])
def test_get_pet_by_status(api_client, status, code):
    query = {"status": status}
    response = api_client.get_pets_by_status(query)
    json_response = response.json()
    pets = [PetModel.model_validate(obj) for obj in json_response]
    assert response.status_code == code
    if pets:
        assert pets[0].id >= 0
    for pet in pets:
        assert pet.status == status
    assert "Content-Type, api_key, Authorization" == response.headers.get("access-control-allow-headers")
    assert "application/json" == response.headers.get("content-type")


@allure.title("Запрос списка питомцев с невалидными статусами, невалидный тип данных")
@pytest.mark.parametrize(["status", "code"],
                         [("dog", 400), (False, 400), (18, 400)])
def test_invalid_get_pet_by_status(api_client, status, code):
    query = {"status": status}
    response = api_client.get_pets_by_status(query)
    json_response = response.json()
    assert response.status_code == code
    assert json_response

@allure.title("Создание питомца")
def test_create_pet(api_client):
    data = PetModel(name="first dog", photoUrls=[
        "https://www.google.com/imgres?q=%D1%84%D0%BE%D1%82%D0%BE%20%D0%B4%D0%BE%D0%B3%D0%B0&imgurl=https%3A%2F%2Fwww.zootovary.com%2Fuserfiles%2F359_1.jpg&imgrefurl=https%3A%2F%2Fwww.zootovary.com%2Fnemetskii-dog-a-359.html&docid=zWN5FY0uBKs88M&tbnid=ZhRv9oghbmTupM&vet=12ahUKEwie2MXsiJOIAxWUBhAIHYXPJDMQM3oECBsQAA..i&w=600&h=750&hcb=2&ved=2ahUKEwie2MXsiJOIAxWUBhAIHYXPJDMQM3oECBsQAA"])
    response = api_client.create_pet(data=dict(data))
    json_response = response.json()
    print(json_response)
    assert response.status_code == 200
    assert json_response['id'] > 0

@allure.title("Создание питомца с максимальным id")
def test_create_pet_with_max_id(api_client):
    max_id_value = 9223372036854775807
    data = PetModel(id=max_id_value, name="shepherd dog", photoUrls=[])
    response = api_client.create_pet(data=dict(data))
    json_response = response.json()
    assert response.status_code == 200
    assert json_response["id"] == max_id_value

@allure.title("Создание питомца с невалидным id за границами валидации")
def test_create_pet_with_invalid_id(api_client):
    data = PetModel(id=INVALID_ID_VALUE, name="cat", photoUrls=[])
    response = api_client.create_pet(data=dict(data))
    assert response.status_code == 405

@allure.title("Удаление питомца")
def test_delete_pet(api_client, pet_creation):
    response = api_client.delete_pet(pet_id=831)
    assert response.status_code == 200

@allure.title("Получение данных о питомце по id")
def test_get_pet_by_id(api_client, pet_creation, pet_deleting):
    response = api_client.get_pet_by_pet_id(pet_id=831)
    assert response.status_code == 200
    json_response = response.json()
    PetModel.model_validate(json_response)

@allure.title("Получение данных о несуществующем питомце по id")
def test_get_pet_by_not_existing_id(api_client):
    response = api_client.get_pet_by_pet_id(pet_id=6324978365)
    assert response.status_code == 404

@allure.title("Получение данных о питомце по невалидному id за границами валидации")
def test_get_pet_by_invalid_id(api_client):
    response = api_client.get_pet_by_pet_id(pet_id=INVALID_ID_VALUE)
    assert response.status_code == 400

@allure.title("Обновление данных питомца")
def test_update_pet(api_client, pet_creation, pet_deleting):
    _id = 831
    params = {"name": "Cherry", "status": "sold"}
    response = api_client.update_pet(pet_id=_id, params=params)
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["message"] == str(_id)

@allure.title("Обновление данных питомца с невалидными параметрами, невалидный тип данных")
def test_update_pet_invalid_params(api_client, pet_creation, pet_deleting):
    _id = 831
    params = {"name": False, "status": 16}
    response = api_client.update_pet(pet_id=_id, params=params)
    assert response.status_code == 405
