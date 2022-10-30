from sqlalchemy.orm import Session
from sqlalchemy import select


from models.CategoryModel import CategoryModel
from schemas.CategorySchema import CategorySchemaCreate


class CategoryService:

    def __init__(self, session: Session):
        self.session = session

    async def create(self, category: CategorySchemaCreate):
        new_category = CategoryModel(name=category.name_category)
        self.session.add(new_category)
        await self.session.flush()



    async def get_all(self):
        query = select(CategoryModel)
        result = await self.session.execute(query)
        return result.scalars().all()


    async def get_by_id(self, id: int):
        query = select(CategoryModel).where(CategoryModel.id_category == id)
        result = await self.session.execute(query)
        return result.scalars().first()



    async def update(self, id: int, category: CategoryModel):

        categoryUpdate = self.session.query(CategoryModel).get(category.id_category)
        categoryUpdate.name_category = category.name
        await self.session.commit()
        return categoryUpdate

    async def delete(self, id: int):
        category = self.session.query(CategoryModel).get(id)
        self.session.delete(category)
        await self.session.commit()
        return category
    

    
