from pydantic import BaseModel
from typing import Optional


class AddressSchema(BaseModel):
    street: str
    number: int
    complement: str
    city: str
    state: str
    cep: str
    user_id: int
    class Config:
        orm_mode = True



class AddressSchemaCreate(AddressSchema):
    id_address: Optional[int] = None
    

class AddressSchemaUp(AddressSchema):
    street: Optional[str]
    number: Optional[int]
    complement: Optional[str]
    city: Optional[str]
    state: Optional[str]
    cep: Optional[str]
    user_id: Optional[int]