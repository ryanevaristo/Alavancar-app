from pydantic import BaseModel, EmailStr
from typing import Optional, List
from schemas.CategorySchema import CategorySchemaCreate
from schemas.AddressSchema import AddressSchema


class UserSchemaBase(BaseModel):
    id_user: Optional[int]
    name: str
    age: int
    email: EmailStr 
    fone: str
    instagram: str

    class config:
        orm_mode: True


class UserSchemaCreate(UserSchemaBase):
    senha: str


class UserSchemaAddress(UserSchemaBase):
    address: Optional[List[AddressSchema]]= []

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
    category: Optional[List[CategorySchemaCreate]]
    func: bool

class UserEnterpriseSchemaCreate(UserEnterpriseSchema):
    senha: str

class UserEnterpriseSchemaUp(UserSchemaBase):
    cnpj: Optional[str]
    city: Optional[str]
    state: Optional[str]
    cep: Optional[str]
    category: Optional[List[CategorySchemaCreate]]
    func: Optional[bool]
