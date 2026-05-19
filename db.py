import mysql.connector
# Importing MySQL connector library
# Used to connect Python with MySQL database


def get_db():
# Dependency function
# FastAPI will use this function with Depends()
# Responsible for DB connection lifecycle


    conn = mysql.connector.connect(
        host= "localhost",
        user="root",
        password="krati",
        database="fast_api_project"
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
        
    