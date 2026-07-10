from fastapi import FastAPI
from .database.database import Base, engine
from .models import models
from app.routers import usuarios

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(usuarios.router)