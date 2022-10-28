from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship

from core.config import settings


class UserEnterprise(settings.DBBaseModel):
    __tablename__ = 'usersEnterprise'

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=True)
    age = Column
    email = Column(String(256), index=True, nullable=False, unique=True)
    fone = Column(String(256), indx=True, nullable=False, unique=True)
    address = Column(String(350), indx=True, nullable=False, unique=True)
    instagram = Column(String(256), indx=True, nullable=False, unique=True)
    senha = Column(String(256), indx=True, nullable=False, unique=True)
    cnpj = Column(String(256, indx=True, nullable=False, unique=True))
    city = Column(String(256, indx=True, nullable=False, unique=True))
    state = Column(String(256, indx=True, nullable=False, unique=True))
    cep = Column(String(256, indx=True, nullable=False, unique=True))
    category = Column(String(256, indx=True, nullable=False, unique=True))
    id_category = Column(Integer, autoincrement=True)
    func = Column(Boolean)

    address = relationship('Address',
                           back_populates="user"
                           )
    category = relationship('Category',
                            back_populates='user'
                            )
