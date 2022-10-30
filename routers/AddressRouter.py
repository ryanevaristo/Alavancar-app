from fastapi import APIRouter, Depends, HTTPException, status, Response

from sqlalchemy.ext.asyncio import AsyncSession

from schemas.AddressSchema import AddressSchemaCreate, AddressSchemaUp

from core.deps import get_session

from services.AddressService import AddressService

router = APIRouter()

# POST /address
@router.post("/address", status_code=status.HTTP_201_CREATED, response_model=AddressSchemaCreate)
async def create_address(address: AddressSchemaCreate, session: AsyncSession = Depends(get_session)):
    try:
        service = AddressService(session)
        await service.create(address)
        return address
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# GET /address
@router.get("/address", status_code=status.HTTP_200_OK, response_model=list[AddressSchemaCreate])
async def get_address(session: AsyncSession = Depends(get_session)):
    try:
        service = AddressService(session)
        return await service.get_all()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# GET /address/{id}
@router.get("/address/{ind}", status_code=status.HTTP_200_OK, response_model=AddressSchemaCreate)
async def get_address_by_id(id: int, session: AsyncSession = Depends(get_session)):
    try:
        service = AddressService(session)
        return await service.get_by_id(id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# PUT /address/{id}
@router.put("/address/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=AddressSchemaCreate)
async def update_address(id: int, address: AddressSchemaUp, session: AsyncSession = Depends(get_session)):
    try:
        service = AddressService(session)
        return await service.update(id, address)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# DELETE /address/{id}
@router.delete("/address/{id}", status_code=status.HTTP_200_OK, response_model=AddressSchemaCreate)
async def delete_address(id: int, session: AsyncSession = Depends(get_session)):
    try:
        service = AddressService(session)
        await service.delete(id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))