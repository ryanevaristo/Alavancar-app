from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship

from core.config import settings


class CategoryModel(settings.DBBasemodel):
    __tablename__ = 'category'

    id_category = Column(Integer, primary_key=True, autoincrement=True)
    name_category = Column(String(256), indx=True, nullable=False, unique=True)

    user = relationship("Usuario",
                        back_populates="category",
                        uselist=False)
