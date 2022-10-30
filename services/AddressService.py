from sqlalchemy.orm import Session
from sqlalchemy import delete, select, update

from models.AddressModel import AddressModel

from schemas.AddressSchema import AddressSchemaCreate

class AddressService:

    def __init__(self, session: Session):
        self.session = session

    async def create(self, address: AddressSchemaCreate):
        new_address = AddressModel(
            street=address.street,
            number=address.number,
            complement=address.complement,
            city=address.city,
            state=address.state,
            cep=address.cep
        )
        self.session.add(new_address)
        await self.session.commit()

    async def get_all(self):
        query = select(AddressModel)
        result: AddressModel = await self.session.execute(query)
        return result.scalars().all()

    async def get_by_id(self, id: int):
        query = select(AddressModel).where(AddressModel.id_address == id)
        result = await self.session.execute(query)
        address: AddressModel = result.scalars().unique().one_or_none()

        return address

    async def update(self, id: int, address: AddressModel):
        query = select(AddressModel).where(AddressModel.id_address == id)
        result = await self.session.execute(query)
        address_update: AddressModel = result.scalars().unique().one_or_none()
        address_update.street = address.street
        address_update.number = address.number
        address_update.complement = address.complement
        address_update.city = address.city
        address_update.state = address.state
        address_update.cep = address.cep
        await self.session.commit()
        return address_update

    async def delete(self, id: int):
        query = delete(AddressModel).where(AddressModel.id_address == id)
        addressDelete: AddressModel = await self.session.execute(query)
        await self.session.commit()
        return addressDelete