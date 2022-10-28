from pydantic import BaseModel
from typing import Optional


class CategorySchema(BaseModel):
    id_category: int
    name_category: str


class config:
    orm_mode: True


class CategorySchemaUp(BaseModel):
    name_category: Optional[str]
