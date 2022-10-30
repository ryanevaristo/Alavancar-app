from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship


from core.config import settings

class CategoryModel(settings.DBBaseModel):
    __tablename__ = 'category'

    id_category = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=True)
    created: relationship = relationship("UserModel", back_populates='category')