from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship

from core.config import settings


class UserModel(settings.DBBasemodel):
    __tablename__ = 'users'

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=True)
    age = Column(Integer, index=True, nullable=False, unique=True)
    email = Column(String(256), index=True, nullable=False, unique=True)
    fone = Column(String(256), indx=True, nullable=False, unique=True)
    address = Column(String(350), indx=True, nullable=False, unique=True)
    instagram = Column(String(256), indx=True, nullable=False, unique=True)
    senha = Column(String(256), indx=True, nullable=False, unique=True)

    address = relationship('Address',
                           back_populates="user"
                           )
    category = relationship('Category',
                            back_populates='user'
                            )
