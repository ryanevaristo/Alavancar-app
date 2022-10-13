from pydantic import BaseModel, EmailStr
from typing import Optional

class ContatosSchema(BaseModel):
    id_contato: Optional[int]
    nome: str
    email: EmailStr
    telefone: str
    instagram: str
    class Config:
        orm_mode = True