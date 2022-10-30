from fastapi import APIRouter, Depends, HTTPException, Response, status


from sqlalchemy.ext.asyncio import AsyncSession

from schemas.CategorySchema import CategorySchemaCreate, CategorySchema

from core.deps import get_session

from services.CategoryService import CategoryService


router = APIRouter()

# POST /category
@router.post("/category", status_code=status.HTTP_201_CREATED, response_model=CategorySchema)
async def create_category(category: CategorySchemaCreate, session: AsyncSession = Depends(get_session)):
    try:
        service = CategoryService(session)
        await service.create(category)
        return category
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# GET /category
@router.get("/category", status_code=status.HTTP_200_OK, response_model=list[CategorySchema])
async def get_category(session: AsyncSession = Depends(get_session)):
    try:
        service = CategoryService(session)
        return await service.get_all()
        
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))