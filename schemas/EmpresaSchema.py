from pydantic import BaseModel
from typing import Optional, List
from .EnderecoSchema import EnderecoSchema

class EmpresaSchema(BaseModel):
    id_empresa: Optional[int]
    nome: str
    cnpj: str
    telefone: str
    endereco: str
    cidade: str
    estado: str
    cep: str
    class Config:
        orm_mode = True


class EmpresaSchemaEndereco(EmpresaSchema):
    endereco: Optional[List[EnderecoSchema]]

