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


class UserSchemaUp(UserSchema):
    name: Optional[str]
    age: Optional[int]
    email: Optional[EmailStr]
    fone: Optional[str]
    address: Optional[str]
    instagram: Optional[str]
    senha: Optional[str]


class UserEnterpriseSchema(UserSchema):
    cnpj: str
    city: str
    state: str
    cep: str
    category: str
    id_category: Optional[int]
    func: bool


class UserEnterpriseSchemaUp(UserSchema):
    cnpj: Optional[str]
    city: Optional[str]
    state: Optional[str]
    cep: Optional[str]
    category: Optional[str]
    func: Optional[bool]
