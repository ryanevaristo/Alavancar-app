from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship

from core.config import settings

class AddressModel(settings.DBBaseModel):
    __tablename__ = 'address'

    id_address = Column(Integer, primary_key=True, autoincrement=True)
    street = Column(String(256), nullable=True)
    number = Column(Integer, nullable=True)
    complement = Column(String(256), nullable=True)
    city = Column(String(256), nullable=True)
    state = Column(String(256), nullable=True)
    cep = Column(String(256), nullable=True)
    created_user_ad: relationship = relationship(
        "UserModel",
        back_populates="address"
    )
