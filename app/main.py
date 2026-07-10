from fastapi import FastAPI
from .database.database import Base, engine
from .models import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

