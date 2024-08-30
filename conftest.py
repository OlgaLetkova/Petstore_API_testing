import pytest

from petstore_api_client.petstore_api_client import PetstoreApiClient

from petstore_models import UserModel, PetModel


@pytest.fixture(scope="function")
def api_client():
    client = PetstoreApiClient()
    return client

@pytest.fixture()
def user_creation(api_client):
    data = UserModel(id=1, username="i", firstName="Irina", lastName="Popova",
                     email="email", password="Pass", phone="790000000", userStatus=1)
    api_client.create_user(data=dict(data))


@pytest.fixture()
def pet_creation(api_client):
    data = PetModel(id=831, name="Lukky", photoUrls=["https://spitz.su/pomeranian-spitz/Color-cloud-goryachii-chocolate"],
                     status="available")
    api_client.create_pet(data=dict(data))


@pytest.fixture()
def pet_deleting(api_client):
    yield
    api_client.delete_pet(pet_id=831)

@pytest.fixture()
def user_deleting(api_client):
    yield
    api_client.delete_user(username="i")
