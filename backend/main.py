from api import article, auth
from core.config import settings
from database.database import engine, get_db
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.user import User
from sqlalchemy.orm import Session
from starlette.requests import Request

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Range", "X-Total-Count"],
    # expose_headers=[],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(auth.router, prefix="/api", tags=["auth"])
app.include_router(article.router, prefix="/api", tags=["article"])
