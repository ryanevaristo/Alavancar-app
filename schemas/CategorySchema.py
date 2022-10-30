from pydantic import BaseModel
from typing import Optional


class CategorySchemaCreate(BaseModel):
    name: Optional[str]
    class Config:
        orm_mode = True

class CategorySchema(CategorySchemaCreate):
    id_category: Optional[int]
