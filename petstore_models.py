from pydantic import BaseModel
from typing import Optional

class PetStoreBaseModel(BaseModel):
    id: int
    name: str

class CategoryModel(PetStoreBaseModel):
    name: Optional[str] = ""

class TagModel(PetStoreBaseModel):
    pass

class PetModel(PetStoreBaseModel):
    id: Optional[int] = None
    category: Optional[CategoryModel] = None
    name: str
    photoUrls: list
    tags: Optional[list[TagModel]] = None
    status: Optional[str] = None


class UserModel(BaseModel):
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int

class OrderModel(BaseModel):
    id: int
    petId: int
    quantity: int
    shipDate: str
    status: str
    complete: bool
