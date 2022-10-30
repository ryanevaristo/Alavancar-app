from pydantic import BaseModel, EmailStr
from typing import Optional, List
from CategorySchema import CategorySchema
from AddressSchema import AddressSchema


class UserSchemaBase(BaseModel):
    id_user: int
    name: str
    age: int
    email: EmailStr
    fone: str
    address: Optional[List[AddressSchema]]
    instagram: str

    class config:
        orm_mode: True


class UserSchemaCreate(UserSchemaBase):
    senha: str

class UserSchemaUp(UserSchemaBase):
    name: Optional[str]
    age: Optional[int]
    email: Optional[EmailStr]
    fone: Optional[str]
    address: Optional[List[AddressSchema]]
    instagram: Optional[str]
    senha: Optional[str]


class UserEnterpriseSchema(UserSchemaBase):
    cnpj: str
    city: str
    state: str
    cep: str
    category: List[CategorySchema]
    func: bool

class UserEnterpriseSchemaCreate(UserEnterpriseSchema):
    senha: str

class UserEnterpriseSchemaUp(UserSchemaBase):
    cnpj: Optional[str]
    city: Optional[str]
    state: Optional[str]
    cep: Optional[str]
    category: Optional[List[CategorySchema]]
    func: Optional[bool]
