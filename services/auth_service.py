from passlib.context import CryptContext
from schemas import UserCreate, UserLogin
from jose import jwt
from datetime import datetime, timedelta

pwd_context = CryptContext(
    schemes = ["bcrypt"],
    deprecated = "auto"
)
SECRET_KEY = "mysecretkey"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30

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
    