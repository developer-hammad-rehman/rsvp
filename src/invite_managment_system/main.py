from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db.models import *
from .config.db_config import connect_db
from contextlib import asynccontextmanager
from .routes.routes import router
from fastapi.staticfiles import StaticFiles



@asynccontextmanager
async def lifespan(app: FastAPI):
    connect_db()
    yield
   
app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/images" , StaticFiles(directory="storage") , name="images")

app.include_router(router)


def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0" , port=8000, log_level="info")
