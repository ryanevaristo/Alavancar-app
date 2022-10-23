from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship

from core.config import settings


class UserModel(settings.DBBaseModel):
    __tablename__ = 'users'

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=True)
    age = Column
    email = Column(String(256), index=True, nullable=False, unique=True)
    fone = Column(String(256), index=True, nullable=False, unique=True)
    address = Column(String(350), index=True, nullable=False, unique=True)
    instagram = Column(String(256), index=True, nullable=False, unique=True)
    senha = Column(String(256), index=True, nullable=False, unique=True)
