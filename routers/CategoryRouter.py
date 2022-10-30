from models.CategoryModel import CategoryModel
from fastapi import APIRouter, Depends, HTTPException, Response, status


from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.CategorySchema import CategorySchemaCreate, CategorySchema

from core.deps import get_session

from services.CategoryService import CategoryService


router = APIRouter()

# POST /category
@router.post("/category", status_code=status.HTTP_201_CREATED, response_model=CategorySchemaCreate)
async def create_category(category: CategorySchemaCreate, session: AsyncSession = Depends(get_session)):
    try:
        service = CategoryService(session)
        await service.create(category)
        return category
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# GET /category
@router.get("/category", status_code=status.HTTP_200_OK, response_model=list[CategorySchemaCreate])
async def get_category(session: AsyncSession = Depends(get_session)):
    try:
        service = CategoryService(session)
        return await service.get_all()

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

# GET /category/{id}
@router.get("/category/{id}", status_code=status.HTTP_200_OK, response_model=CategorySchemaCreate)
async def get_category_by_id(id: int, session: AsyncSession = Depends(get_session)):
    try:
        service = CategoryService(session)
        return await service.get_by_id(id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# PUT /category/{id}
@router.put("/category/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=CategorySchemaCreate)
async def update_category(id: int, category: CategorySchemaCreate, session: AsyncSession = Depends(get_session)):
    try:
        service = CategoryService(session)
        return await service.update(id, category)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# DELETE /category/{id}
@router.delete("/category/{id}", status_code=status.HTTP_200_OK, response_model=CategorySchemaCreate)
async def delete_category(id: int, session: AsyncSession = Depends(get_session)):
    try:
        service = CategoryService(session)
        await service.delete(id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))