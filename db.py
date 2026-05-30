import mysql.connector
from dotenv import load_dotenv
import os
# Importing MySQL connector library
# Used to connect Python with MySQL database

load_dotenv(dotenv_path=".env")

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "krati")
DB_NAME = os.getenv("DB_NAME", "fast_api_project")

def get_db():
# Dependency function
# FastAPI will use this function with Depends()
# Responsible for DB connection lifecycle


    conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME

    )
    
    # Database Connection Creation
    # Establishes connection between backend and MySQL database
    # conn object is used for:
    # - transactions
    # - commit()
    # - rollback()


    cursor = conn.cursor(dictionary = True)
    
    # Cursor Creation
    # Cursor is used to execute SQL queries
    
    # dictionary=True means:
    # Query results return as dictionaries
    
    # Example:
    # {"name": "Krati"}
    
    # instead of:
    # ("Krati",)


    try:
        yield conn, cursor
        
        # Dependency Injection Return
        
        # Whatever is yielded here
        # gets injected into route
        
        # Example:
        # db_tuple = Depends(get_db)
        
        # becomes:
        # db_tuple = (conn, cursor)
        
        
        # yield pauses function temporarily
        # allows cleanup after request finishes
        
        
        # Difference:
        
        # return:
        # gives value once and exits immediately
        
        # yield:
        # gives value
        # pauses function
        # resumes later for cleanup


    finally:
        cursor.close()
        conn.close()

        # Cleanup Block
        
        # finally always runs
        # even if error occurs
        
        # Prevents:
        # - memory leaks
        # - hanging DB connections
        # - connection exhaustion
        
    