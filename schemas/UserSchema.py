from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional, List
from schemas.CategorySchema import CategorySchemaCreate
from schemas.AddressSchema import AddressSchemaCreate


class UserSchemaBase(BaseModel):
    id_user: Optional[int] = None
    name: str
    age: date
    email: EmailStr 
    fone: str
    instagram: str

    class Config:
        orm_mode = True


class UserSchemaCreate(UserSchemaBase):
    senha: str


class UserSchemaAddress(UserSchemaCreate):
    address: Optional[List[AddressSchemaCreate]]= []

class UserSchemaUp(UserSchemaBase):
    name: Optional[str]
    age: Optional[date]
    email: Optional[EmailStr]
    fone: Optional[str]
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
