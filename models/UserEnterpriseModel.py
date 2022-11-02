from sqlalchemy import ForeignKey, Integer, String, Column, Boolean, Date, Table
from sqlalchemy.orm import relationship

from core.config import settings

association_table = Table(
    "UserEnterprise_Category",
    settings.DBBaseModel.metadata,
    Column("id_user", ForeignKey("usersEnterprise.id_user")),
    Column("category_id", ForeignKey("category.id_category")),
)


class UserEnterpriseModel(settings.DBBaseModel):
    __tablename__ = 'usersEnterprise'

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=True)
    age = Column(Date, nullable=True)
    email = Column(String(256), index=True, nullable=False, unique=True)
    fone = Column(String(256), index=True, nullable=False, unique=True)
    instagram = Column(String(256), index=True, nullable=False, unique=True)
    senha = Column(String(256), index=True, nullable=False, unique=True)
    cnpj = Column(String(256), index=True, nullable=False, unique=True)
    func = Column(Boolean, default=True)
    category = relationship("CategoryModel", secondary=association_table,
    back_populates='created_user')

    