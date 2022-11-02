from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship
from models.UserEnterpriseModel import association_table


from core.config import settings

class CategoryModel(settings.DBBaseModel):
    __tablename__ = 'category'

    id_category = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=True)
    created_user: relationship = relationship("UserEnterprise", 
    secondary=association_table ,back_populates='category')