from fastapi import APIRouter, Depends

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
    user: UserLogin,
    db=Depends(get_db)
):

    conn, cursor = db

    return authenticate_user(
        user,
        conn,
        cursor
    )
    