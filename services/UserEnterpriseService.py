from sqlalchemy import update, delete
from sqlalchemy.orm import Session, selectinload
from schemas.UserSchema import UserEnterpriseSchema, UserEnterpriseSchemaUp, UserEnterpriseSchemaCreate
from models.UserEnterpriseModel import UserEnterpriseModel
from core.security import generate_hash_password
from core.auth import authentication, criar_token_acesso
from sqlalchemy.future import select

class UserEnterpriseService():
    def __init__(self, session: Session):
        self.session = session
    
    async def create_user_enterprise(self, user_enterprise: UserEnterpriseSchemaCreate):
        new_user = UserEnterpriseModel(
            name=user_enterprise.name,
            age=user_enterprise.age,
            email=user_enterprise.email,
            senha=generate_hash_password(user_enterprise.senha),
            fone=user_enterprise.fone,
            instagram=user_enterprise.instagram,
            cnpj=user_enterprise.cnpj,
            category=user_enterprise.category,
            func=user_enterprise.func

        )
        self.session.add(new_user)
        await self.session.commit()
        return new_user

    async def update_user_enterprise(self, user_enterprise: UserEnterpriseSchemaUp, id: int):
        query = select(UserEnterpriseModel).where(UserEnterpriseModel.id_user == id).options(selectinload(UserEnterpriseModel.category))
        result = await self.session.execute(query)
        user_update: UserEnterpriseModel = result.scalars().unique().one_or_none()
        if user_update:
            user_update.name = user_enterprise.name
            user_update.age = user_enterprise.age
            user_update.email = user_enterprise.email
            user_update.fone = user_enterprise.fone
            user_update.instagram = user_enterprise.instagram
            user_update.cnpj = user_enterprise.cnpj
            user_update.category = user_enterprise.category
            user_update.func = user_enterprise.func

        await self.session.commit()
        return user_update

    async def get_users_enterprise(self):
        query = select(UserEnterpriseModel).options(selectinload(UserEnterpriseModel.category))
        result = await self.session.execute(query)
        return result.scalars().unique().all()

    async def get_by_id_user_enterprise(self, id: int):
        query = select(UserEnterpriseModel).where(UserEnterpriseModel.id_user == id).options(selectinload(UserEnterpriseModel.category))
        result = await self.session.execute(query)
        return result.scalars().unique().one_or_none()

    async def login_user_enterprise(self, user_enterprise: UserEnterpriseSchemaCreate):
        query = select(UserEnterpriseModel).where(UserEnterpriseModel.email == user_enterprise.email)
        result = await self.session.execute(query)
        user_login: UserEnterpriseModel = result.scalars().unique().one_or_none()
        if user_login:
            if authentication(user_enterprise.senha, user_login.senha):
                token = criar_token_acesso(user_login.id_user)
                return token
        return None

    async def delete_user_enterprise(self, id: int):
        query = delete(UserEnterpriseModel).where(UserEnterpriseModel.id_user == id).options(selectinload(UserEnterpriseModel.category))
        user_delete = await self.session.execute(query)
        await self.session.commit()
        return user_delete