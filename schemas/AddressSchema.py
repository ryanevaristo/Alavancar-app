from pydantic import BaseModel

class AddressSchema(BaseModel):
    id_address: int
    cep: int
    public_place: str
    house_number: int
    city: str
    state: str

    class config:
        orm_mode: True
