from pydantic import BaseModel
from typing import Optional

class EnderecoSchema(BaseModel):
    id_endereco: Optional[int]
    rua: str
    numero: str
    complemento: str
    bairro: str
    cep: str
    class Config:
        orm_mode = True
