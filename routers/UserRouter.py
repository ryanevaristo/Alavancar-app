from typing import Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status, Response

from sqlalchemy.ext.asyncio import AsyncSession

from schemas.UserSchema import UserSchemaBase, UserSchemaUp, UserSchemaCreate, UserSchemaAddress

from core.deps import get_session

from services.UserService import UserService


router = APIRouter()

# POST /user
@router.post("/user", status_code=status.HTTP_201_CREATED, response_model=UserSchemaBase)
async def create_user(user: UserSchemaCreate, session: AsyncSession = Depends(get_session)):
    try:
        service = UserService(session)
        await service.create(user)
        return user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

# GET /user
@router.get("/user", status_code=status.HTTP_200_OK, response_model=List[UserSchemaBase])
async def get_user(session: AsyncSession = Depends(get_session)):
    try:
        service = UserService(session)
        return await service.get_users()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

# GET /user/{id}
@router.get("/user/{id}", status_code=status.HTTP_200_OK, response_model=UserSchemaBase)
async def get_user_by_id(id: int, session: AsyncSession = Depends(get_session)):
    try:
        service = UserService(session)
        return await service.get_by_id(id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

# PUT /user
@router.put("/user/{id}", status_code=status.HTTP_200_OK, response_model=UserSchemaUp)
async def update_user(id: int, user: UserSchemaUp, session: AsyncSession = Depends(get_session)):
    try:
        service = UserService(session)
        return await service.update(user,id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

# DELETE /user/{id}
@router.delete("/user/{id}", status_code=status.HTTP_200_OK, response_model=UserSchemaBase)
async def delete_user(id: int, session: AsyncSession = Depends(get_session)):
    try:
        service = UserService(session)
        await service.delete(id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))