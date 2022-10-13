from pydantic import BaseModel
from typing import Optional


class CategorySchema(BaseModel):
    id_category: Optional[int]
    name: str
    class Config:
        orm_mode = True