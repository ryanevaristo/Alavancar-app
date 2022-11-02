from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.ext.asyncio import AsyncSession
from core.config import settings
from core.deps import get_session
from typing import List
 


from schemas.UserSchema import UserEnterpriseSchema, UserEnterpriseSchemaUp, UserEnterpriseSchemaCreate
from services.UserEnterpriseService import UserEnterpriseService


router = APIRouter()


# POST /user
@router.post("/user",status_code=status.HTTP_201_CREATED, response_model=UserEnterpriseSchema)
async def create_user(user: UserEnterpriseSchemaCreate, session: AsyncSession = Depends(get_session)):
    try:
        service = UserEnterpriseService(session)
        return await service.create_user_enterprise(user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# GET /users
@router.get("/users_enterprise", status_code=status.HTTP_200_OK, response_model=List[UserEnterpriseSchema])
async def get_user(session: AsyncSession = Depends(get_session)):
    try:
        service = UserEnterpriseService(session)
        return await service.get_users_enterprise()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# GET /user/{id}
@router.get("/user_enterprise/{id}", status_code=status.HTTP_200_OK, response_model=UserEnterpriseSchema)
async def get_user_by_id(id: int, session: AsyncSession = Depends(get_session)):
    try:
        service = UserEnterpriseService(session)
        return await service.get_by_id_user_enterprise(id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

# PUT /user/{id}
@router.put("/user_enterprise/{id}", status_code=status.HTTP_200_OK, response_model=UserEnterpriseSchema)
async def update_user(id: int, user: UserEnterpriseSchemaUp, session: AsyncSession = Depends(get_session)):
    try:
        service = UserEnterpriseService(session)
        return await service.update_user_enterprise(user, id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

# DELETE /user/{id}
@router.delete("/user_enterprise/{id}", status_code=status.HTTP_200_OK)
async def delete_user(id: int, session: AsyncSession = Depends(get_session)):
    try:
        service = UserEnterpriseService(session)
        await service.delete_user_enterprise(id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

