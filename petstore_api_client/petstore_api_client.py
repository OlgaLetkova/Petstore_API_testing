import requests


class PetstoreApiClient:

    def __init__(self,
                 base_url="https://petstore.swagger.io/v2",
                 auth_token="special-key"):
        self.session = requests.Session()
        self.session.headers = {"Authorization": f"{auth_token}",
                                "Content-Type": "application/json"}
        self.session.verify = False
        self.base_url = base_url

    def get_pets_by_status(self, query):
        response = self.session.get(url=f"{self.base_url}/pet/findByStatus",
                                    params=query)
        return response

    def create_pet(self, data):
        response = self.session.post(f"{self.base_url}/pet",
                                     json=data)
        return response

    def delete_pet(self, pet_id):
        response = self.session.delete(f"{self.base_url}/pet/{pet_id}")
        return response

    def get_pet_by_pet_id(self, pet_id):
        response = self.session.get(f"{self.base_url}/pet/{pet_id}")
        return response

    def update_pet(self, pet_id, params):
        headers_update = {"Authorization": "special-key",
                         "Content-Type": "application/x-www-form-urlencoded"}
        response = self.session.post(f"{self.base_url}/pet/{pet_id}", params=params, headers=headers_update)
        return response

    def create_user(self, data):
        response = self.session.post(f"{self.base_url}/user",
                                     json=data)
        return response

    def delete_user(self, username):
        response = self.session.delete(f"{self.base_url}/user/{username}")
        return response

    def get_user_by_username(self, username):
        response = self.session.get(f"{self.base_url}/user/{username}")
        return response

    def update_user(self, username, params):
        response = self.session.put(f"{self.base_url}/user/{username}", json=params)
        return response

    def get_pet_inventory(self):
        response = self.session.get(f"{self.base_url}/store/inventory")
        return response

    def order_pet(self, data):
        response = self.session.post(f"{self.base_url}/store/order",
                                     json=data)
        return response
