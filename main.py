from fastapi import FastAPI
from core.config import settings
from routers.CategoryRouter import router as router_category



app = FastAPI(title="Alavancar Motion", version="0.0.1")
app.include_router(router=router_category, prefix='/app/v1', tags=['category'])



if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                 reload=True)