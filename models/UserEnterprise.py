from sqlalchemy import ForeignKey, Integer, String, Column, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from core.config import settings


class UserEnterprise(settings.DBBaseModel):
    __tablename__ = 'usersEnterprise'

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=True)
    age = Column
    email = Column(String(256), index=True, nullable=False, unique=True)
    fone = Column(String(256), index=True, nullable=False, unique=True)
    instagram = Column(String(256), index=True, nullable=False, unique=True)
    senha = Column(String(256), index=True, nullable=False, unique=True)
    cnpj = Column(String(256), index=True, nullable=False, unique=True)
    city = Column(String(256), index=True, nullable=False, unique=True)
    state = Column(String(256), index=True, nullable=False, unique=True)
    cep = Column(String(256), index=True, nullable=False, unique=True)
    func = Column(Boolean)
    category_id = Column(Integer, ForeignKey('category.id_category'))
    category: relationship = relationship(
        "CategoryModel",
        back_populates="created_user"
    )