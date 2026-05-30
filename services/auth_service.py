
from passlib.context import CryptContext
from schemas import UserCreate, UserLogin
from jose import jwt, JWTError
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

pwd_context = CryptContext(
    schemes = ["bcrypt"],
    deprecated = "auto"
)
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "mysecretkey"
)

ALGORITHM = os.getenv(
    "ALGORITHM",
    "HS256"
)

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv(
        "ACCESS_TOKEN_EXPIRE_MINUTES",
        "30"
    )
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/login"
)

def hash_password (password: str):
    return pwd_context.hash(password)


def verify_password (plain_password: str, hashed_password:str):\
    return pwd_context.verify(
        plain_password,
        hashed_password
    )
    

def create_user(user: UserCreate, conn, cursor):
    hashed_password = hash_password(user.password)
    
    query = """
    INSERT INTO users (name, email, hashed_password)
    VALUES (%s, %s, %s)
    """

    values = (
        user.name,
        user.email,
        hashed_password
    )
    
    cursor.execute(query, values)
    
    conn.commit()
    
    return {
        "message": "User Created Successfully"
    }

def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({
        "exp": expire
    })

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt

def authenticate_user(
    user: UserLogin,
    conn,
    cursor
):
    query = """
    SELECT * FROM users
    WHERE email = %s
    """

    cursor.execute(query, (user.email,))

    db_user = cursor.fetchone()

    if not db_user:

        return {
            "error": "Invalid email or password"
        }

    stored_password = db_user["hashed_password"]

    is_valid = verify_password(
        user.password,
        stored_password
    )

    if not is_valid:

        return {
            "error": "Invalid email or password"
        }

    access_token = create_access_token(
        {
            "user_id": db_user["id"],
"email": db_user["email"]
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

def get_current_user(
    token: str = Depends(oauth2_scheme)

):
    print("TOKEN RECEIVED:", token)
    credentials_exception = HTTPException(
    status_code=401,
    detail="Could not validate credentials"
    )

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("user_id")

        email = payload.get("email")

        if user_id is None or email is None:

            raise credentials_exception

        return {
            "user_id": user_id,
            "email": email
        }

    except JWTError:

        raise credentials_exception
    
    
    