from fastapi import APIRouter, Depends, HTTPException, status, Response

from sqlalchemy.ext.asyncio import AsyncSession

from schemas.UserSchema import UserSchemaBase, UserSchemaUp, UserSchemaCreate

from core.deps import get_session

from services.UserService import UserService


router = APIRouter()

# POST /user
@router.post("/user", status_code=status.HTTP_201_CREATED, response_model=UserSchemaCreate)
async def create_user(user: UserSchemaCreate, session: AsyncSession = Depends(get_session)):
    try:
        service = UserService(session)
        await service.create(user)
        return user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

