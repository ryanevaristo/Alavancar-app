from pydantic import BaseModel
from typing import Optional


class AddressSchema(BaseModel):
    id_address: int
    cep: int
    public_place: str
    house_number: int
    city: str
    state: str

    class config:
        orm_mode: True


class AddressSchema(BaseModel):
    cep: Optional[int]
    public_place: Optional[str]
    house_number: Optional[int]
    city: Optional[str]
    state: Optional[str]
