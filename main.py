from fastapi import FastAPI
from core.config import settings



app = FastAPI(title="Alavancar Motion", version="0.0.1")




if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                 reload=True)