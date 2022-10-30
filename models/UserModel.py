from unicodedata import category
from sqlalchemy import ForeignKey, Integer, String, Column, Boolean
from sqlalchemy.orm import relationship

from core.config import settings


class UserModel(settings.DBBaseModel):
    __tablename__ = 'users'

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=True)
    age = Column
    email = Column(String(256), index=True, nullable=False, unique=True)
    fone = Column(String(256), index=True, nullable=False, unique=True)
    instagram = Column(String(256), index=True, nullable=False, unique=True)
    senha = Column(String(256), index=True, nullable=False, unique=True)
    category_id = Column(Integer, ForeignKey('category.id_category'))
    address_id = Column(Integer, ForeignKey('address.id_address'))
    category: relationship = relationship(
        "CategoryModel",
        back_populates="created_user"
    )
    address: relationship = relationship(
        "AddressModel",
        back_populates="created_user_ad",
        uselist=True,
        lazy="joined"

    )
