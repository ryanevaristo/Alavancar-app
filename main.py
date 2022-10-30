from fastapi import FastAPI
from core.config import settings
from routers.CategoryRouter import router as router_category
from routers.AddressRouter import router as router_address



app = FastAPI(title="Alavancar Motion", version="0.0.1")
app.include_router(router=router_category, prefix=settings.API_V1_STR, tags=['category'])
app.include_router(router=router_address, prefix=settings.API_V1_STR, tags=['address'])




if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                 reload=True)