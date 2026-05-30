from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from schemas import UserCreate, UserLogin
from db import get_db

from services.auth_service import create_user
from services.auth_service import (
    create_user,
    authenticate_user
)

router = APIRouter()

@router.post("/signup")
def signup(
    user: UserCreate,
    db = Depends(get_db)
):
    
    conn, cursor = db
    
    return create_user(
        user,
        conn,
        cursor
    )
    
@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db=Depends(get_db)
):

    print("LOGIN HIT")
    print(form_data.username)
    print(form_data.password)

    conn, cursor = db

    user_data = UserLogin(
        email=form_data.username,
        password=form_data.password
    )

    return authenticate_user(
        user_data,
        conn,
        cursor
    )