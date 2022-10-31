from typing import Optional
from sqlalchemy.orm import Session
from schemas.UserSchema import UserSchemaBase, UserSchemaUp, UserSchemaCreate
from models.UserModel import UserModel
from core.security import generate_hash_password
from core.auth import authentication, criar_token_acesso
from sqlalchemy.future import select
from sqlalchemy import  delete, update


class UserService():
    def __init__(self, session: Session):
        self.session = session

    async def create(self, user: UserSchemaCreate):
        new_user = UserModel(
            name=user.name,
            age=user.age,
            email=user.email,
            senha=generate_hash_password(user.senha),
            fone=user.fone,
            instagram=user.instagram
        )

        self.session.add(new_user)
        await self.session.commit()
        return new_user

    async def update(self, user: UserSchemaUp, id: int):
        query = select(UserModel).where(UserModel.id_user == id)
        result = await self.session.execute(query)
        user_update: UserModel = result.scalars().unique().one_or_none()
        if user_update:
            user_update.name = user.name
            user_update.age = user.age
            user_update.email = user.email
            user_update.fone = user.fone
            user_update.instagram = user.instagram

        await self.session.commit()
        return user_update

    async def get_users(self):
        query = select(UserModel)
        result = await self.session.execute(query)
        return result.scalars().unique().all()
    
    async def get_by_id(self, id: int):
        query = select(UserModel).where(UserModel.id_user == id)
        result = await self.session.execute(query)
        return result.scalars().unique().one_or_none()



    async def login(self, user: UserSchemaBase):
        query = select(UserModel).where(UserModel.email == user.email)
        result = await self.session.execute(query)
        user_login: UserModel = result.scalars().unique().one_or_none()
        if user_login:
            if authentication(user.senha, user_login.senha):
                return criar_token_acesso(user_login.id_user)
        return None

    async def update_senha(self, user: UserSchemaUp, id: int):
        query = select(UserModel).where(UserModel.id_user == id)
        result = await self.session.execute(query)
        user_update: UserModel = result.scalars().unique().one_or_none()
        if user_update:
            user_update.senha = generate_hash_password(user.senha)

        await self.session.commit()
        return user_update
        

    async def delete(self, id: int):
        query = delete(UserModel).where(UserModel.id_user == id)
        userDelete: UserModel = await self.session.execute(query)
        await self.session.commit()
        return userDelete

    async def get_email(self, email: str):
        query = select(UserModel).where(UserModel.email == email)
        return self.session.execute(query)