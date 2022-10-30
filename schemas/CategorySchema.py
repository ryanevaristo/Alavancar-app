from pydantic import BaseModel
from typing import Optional


class CategorySchema(BaseModel):
    name_category: Optional[str]

class CategorySchemaCreate(BaseModel):
    id_category: Optional[int]
    name_category: Optional[str]


class config:
    orm_mode: True


class CategorySchemaUp(BaseModel):
    name_category: Optional[str]