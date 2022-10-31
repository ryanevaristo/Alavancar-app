from unicodedata import category
from sqlalchemy import ForeignKey, Integer, String, Column, Boolean, Date
from sqlalchemy.orm import relationship

from core.config import settings


class UserModel(settings.DBBaseModel):
    __tablename__ = 'users'

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=True)
    age = Column(Date, nullable=True)
    email = Column(String(256), index=True, nullable=False, unique=True)
    fone = Column(String(256), index=True, nullable=False, unique=True)
    instagram = Column(String(256), index=True, nullable=False, unique=True)
    senha = Column(String(256), index=True, nullable=False, unique=True)
    address: relationship = relationship(
        "AddressModel",
        cascade="all,delete-orphan",
        back_populates="create_ad",
        uselist=True,
        lazy="joined"
    )
