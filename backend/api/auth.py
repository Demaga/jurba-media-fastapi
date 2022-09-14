import json
from datetime import datetime, timedelta

from core import auth, security
from core.config import settings
from crud.user import *
from database.database import get_db
from fastapi import APIRouter, Depends, Form, HTTPException, Response, status
from schemas.auth import Token, TokenData
from schemas.user import User, UserCreate
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/token", response_model=Token)
def login(db: Session = Depends(get_db), email: str = Form(), password: str = Form()):
    user = auth.authenticate_user(db, email, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users", response_model=list[User])
def read_users(response: Response, db: Session = Depends(get_db)):
    users = get_users(db)
    # This is necessary for react-admin to work
    response.headers["Content-Range"] = f"0-9/{len(users)}"
    return users


@router.get("/users/me/", response_model=User)
def read_users_me(current_user: User = Depends(auth.get_current_active_user)):
    return current_user


@router.get("/users/me/items/")
def read_own_items(current_user: User = Depends(auth.get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.email}]
