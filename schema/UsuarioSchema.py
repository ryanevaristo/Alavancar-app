from pydantic import BaseModel, EmailStr
from typing import Optional


class UserSchema(BaseModel):
    id_user: int
    name: str
    age: int
    email: EmailStr
    fone: str
    address: str
    instagram: str
    senha: str

    class config:
        orm_mode: True


class UserEnterpriseSchema(UserSchema):
    cnpj: str
    city: str
    state: str
    cep: str
    category: str
    id_category: Optional[int]
    func: bool
