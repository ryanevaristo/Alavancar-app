from tokenize import String
from sqlalchemy import Column, Integer, String, BOOLEAN
from sqlalchemy.orm import relationship

from core.config import settings


class AddressModel(settings.DBBaseModel):
    __tablename__ = 'Address'

    id_address = Column(Integer, primary_key=True, autoincrement=True)
    cep = Column(Integer, index=True, nullable=False, unique=True)
    public_place = Column(String(256), indx=True, nullable=False, unique=True)
    house_number = Column(Integer, index=True, nullable=False, unique=True)
    city = Column(String(256), indx=True, nullable=False, unique=True)
    state = Column(String(256), indx=True, nullable=False, unique=True)

    user = relationship("Usuario",
                        back_populates="address",
                        uselist=False)
