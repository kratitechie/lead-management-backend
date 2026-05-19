def create_lead_services(conn, cursor, lead):

    query = """
    INSERT INTO leads
    (name, phone, email, requirement, budget, location, stage, loan_required)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        lead.name,
        lead.phone,
        lead.email,
        lead.requirement,
        lead.budget,
        lead.location,
        lead.stage,
        lead.loan_required
    )

    cursor.execute(query, values)

    conn.commit()

    return {"message":"Lead stored successfully"}

def fetch_leads(
    cursor,
    location=None,
    budget=None,
    stage=None
):

    # Service Layer Function
    # Contains business/query logic
    # Independent of FastAPI routes

    query = "SELECT * FROM leads WHERE 1=1"

    # Base SQL Query
    
    # 1=1 is used for dynamic query building
    
    # Makes appending conditions easier:
    # AND location = ...
    # AND budget = ...
    values = []

    # Stores dynamic query values
    # Used for parameterized SQL queries


    if location:

        # Conditional Filtering Logic
        # Runs only if location filter is provided

        query += " AND location = %s"

        # Dynamically extends SQL query

        values.append(location)

        # Adds filter value safely
        # Prevents SQL Injection


    if budget:

        query += " AND budget = %s"

        values.append(budget)


    if stage:

        query += " AND stage = %s"

        values.append(stage)


    cursor.execute(query, tuple(values))

    # SQL Execution
    
    # tuple(values):
    # Converts list into SQL-compatible tuple
    
    # Executes parameterized query safely


    return cursor.fetchall()

    # Fetches all matching rows
    
    # Returns list of dictionaries
    # because dictionary=True was used in cursor
    
def get_id(
    conn,
    cursor, 
    id
):
    query = "SELECT * FROM leads WHERE id=%s"
        # SQL SELECT query

    cursor.execute(query,(id,))
        # Parameterized query execution

    lead = cursor.fetchone()
        # Fetch single row

    if lead:
        return lead

        return {"message":"Lead not found"}
    
def update_leads(
    conn, cursor, lead
    ):

    update_fields = []
    values = []

        # Dynamic query preparation

    if lead.name is not None:
        update_fields.append("name=%s")
        values.append(lead.name)

    if lead.phone is not None:
        update_fields.append("phone=%s")
        values.append(lead.phone)

    if lead.email is not None:
        update_fields.append("email=%s")
        values.append(lead.email)

    if lead.requirement is not None:
        update_fields.append("requirement=%s")
        values.append(lead.requirement)

    if lead.budget is not None:
        update_fields.append("budget=%s")
        values.append(lead.budget)

    if lead.location is not None:
        update_fields.append("location=%s")
        values.append(lead.location)

    if lead.stage is not None:
        update_fields.append("stage=%s")
        values.append(lead.stage)

    if lead.loan_required is not None:
        update_fields.append("loan_required=%s")
        values.append(lead.loan_required)

        # Conditional update logic
        # Only updates fields provided by client

    if not update_fields:
        return {"message":"No fields to update"}

    query = f"""
    UPDATE leads
    SET {', '.join(update_fields)}
    WHERE id=%s
    """
        # Dynamic UPDATE query

    values.append(id)

    cursor.execute(query, tuple(values))
    # Executes UPDATE query

    conn.commit()
        # Saves updated changes

    return {"message":"Lead updated successfully"}


def delete_leads(
    conn, cursor, lead
):

    query = "DELETE FROM leads WHERE id=%s"
        # SQL DELETE query

    cursor.execute(query,(id,))
        # Executes DELETE operation

    conn.commit()
        # Saves deletion permanently

    if cursor.rowcount > 0:
            # Checks whether row was deleted

        return {"message":"Lead deleted successfully"}

    return {"message":"Lead not found"}