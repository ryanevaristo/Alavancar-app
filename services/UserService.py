from ast import Delete
from email.headerregistry import Address
from multiprocessing import synchronize
from turtle import update
from typing import Optional
from typing_extensions import Self
from sqlalchemy.orm import Session
from schema.UsuarioSchema import UserSchema, UserSchemaUp
from models.Usuario import UserModel
from core.security import generate_hash_password
from core.auth import authentication, criar_token_acesso
from sqlalchemy.future import select


class User():
    def __init__(self, db: Session):
        self.db = db

    async def create_user(self, user: UserSchema):
        new_user = UserModel(
            name=user.name,
            age=user.age,
            email=user.email,
            senha=generate_hash_password(user.senha),
            fone=user.fone,
            address=user.address,
            instagram=user.instagram
        )

        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    async def Update(self, user: UserSchemaUp, id: int):
        update_user = (
            update(UserModel).where(UserModel.id_user == id).values(
                **user.dict()).execution_options(synchronize_session="fetch")
        )

        await self.db.execute(update_user)
        return user.dict()

    async def List_users(self, id: Optional[int]):
        if (id):
            query = select(UserModel).where(UserModel.id_user == id)
            result = await self.db.execute(query)
            return result.one()
        else:
            query = select(UserModel)
            result = await self.db.execute(query)
            return result.scalars().all()

    async def remove(self, id: int):
        query = Delete(UserModel).where(UserModel.id_user == id)
        await self.db.execute(query)

    async def get_email(self, email: str):
        query = select(UserModel).where(UserModel.email == email)
        return self.db.execute(query)


'''
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
        '''
