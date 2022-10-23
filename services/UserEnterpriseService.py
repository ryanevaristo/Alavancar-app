from ast import Delete
from turtle import update
from typing import Optional
from sqlalchemy.orm import Session
from schemas.UserSchema import UserEnterpriseSchema, UserEnterpriseSchemaUp
from models.UsesEnterprise import UserEnterprise
from core.security import generate_hash_password
from core.auth import authentication, criar_token_acesso
from sqlalchemy.future import select


class User():
    def __init__(self, db: Session):
        self.db = db

    async def create_user_enterprise(self, user_enterprise: UserEnterpriseSchema):
        new_user = UserEnterprise(
            name=user_enterprise.name,
            age=user_enterprise.age,
            email=user_enterprise.email,
            senha=generate_hash_password(user_enterprise.senha),
            fone=user_enterprise.fone,
            address=user_enterprise.address,
            instagram=user_enterprise.instagram,
            cnpj=user_enterprise.cnpj,
            city=user_enterprise.city,
            state=user_enterprise.state,
            cep=user_enterprise.cep,
            category=user_enterprise.category,
            func=user_enterprise.func

        )
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    async def Update(self, user_enterprise: UserEnterpriseSchemaUp, id: int):
        update_user = (
            update(UserEnterprise).where(UserEnterprise.id_user == id).values(
                **user_enterprise.dict()).execution_options(synchronize_session="fetch")
        )

        await self.db.execute(update_user)
        return user_enterprise.dict()

    async def List_users(self, id: Optional[int]):
        if (id):
            query = select(UserEnterprise).where(UserEnterprise.id_user == id)
            result = await self.db.execute(query)
            return result.one()
        else:
            query = select(UserEnterprise)
            result = await self.db.execute(query)
            return result.scalars().all()

    async def remove(self, id: int):
        query = Delete(UserEnterprise).where(UserEnterprise.id_user == id)
        await self.db.execute(query)

    async def get_email(self, email: str):
        query = select(UserEnterprise).where(UserEnterprise.email == email)
        return self.db.execute(query)