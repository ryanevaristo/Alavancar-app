from sqlalchemy.orm import Session
from sqlalchemy import delete, select, update


from models.CategoryModel import CategoryModel
from schemas.CategorySchema import CategorySchemaCreate


class CategoryService:

    def __init__(self, session: Session):
        self.session = session

    async def create(self, category: CategorySchemaCreate):
        new_category = CategoryModel(name=category.name)
        self.session.add(new_category)
        await self.session.commit()



    async def get_all(self):
        query = select(CategoryModel)
        result: CategoryModel = await self.session.execute(query)
        return result.scalars().all()


    async def get_by_id(self, id: int):
        query = select(CategoryModel).where(CategoryModel.id_category == id)
        result = await self.session.execute(query)
        category: CategoryModel = result.scalars().unique().one_or_none()
        
        return category



    async def update(self, id: int, category: CategoryModel):
        query = select(CategoryModel).where(CategoryModel.id_category == id)
        result = await self.session.execute(query)
        category_update: CategoryModel = result.scalars().unique().one_or_none()
        category_update.name = category.name
        await self.session.commit()
        return category_update

    async def delete(self, id: int):
        query = delete(CategoryModel).where(CategoryModel.id_category == id)
        categoryDelete: CategoryModel = await self.session.execute(query)
        await self.session.commit()
        return categoryDelete
    

    
