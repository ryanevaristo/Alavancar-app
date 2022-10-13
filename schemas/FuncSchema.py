from pydantic import BaseModel
from typing import Optional


class FuncSchema(BaseModel):
    id_func: Optional[int]
    aberto: bool
    Fechado: bool
    class Config:
        orm_mode = True