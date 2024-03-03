from pydantic import BaseModel

class Customer(BaseModel):
    id: int
    username: str
    address: str

class CustomerCreate(BaseModel):
    username: str
    address: str


customers: list[Customer] = [
    Customer(id=1, username="Faheed", address="15, ajiboye str"),
    Customer(id=2, username="sweetboy", address="28, GRA str")
]