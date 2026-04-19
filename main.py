import mysql.connector
from fastapi import FastAPI
from schemas import LeadCreate, LeadUpdate

app = FastAPI()

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="krati",
    database="fast_api_project"
)

cursor = db.cursor(dictionary=True)

# 🔥 NEW API
from schemas import LeadCreate  # make sure this is added

@app.post("/lead")
def create_lead(lead: LeadCreate):
    try:
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
        db.commit()

        return {"message": "Lead stored successfully"}

    except Exception as e:
        return {"error": str(e)}
    
@app.get("/leads")
def get_leads(location: str = None, budget: str= None, stage: str = None):
    try:
        query = "SELECT * FROM leads WHERE 1=1"
        values = []

        if location:
            query += " AND location = %s"
            values.append(location)
        if budget:
            query += "AND budget = %s"
            values.append(budget)
        if stage:
            query += " AND stage = %s"
            values.append(stage)

        cursor.execute(query, tuple(values))
        result = cursor.fetchall()

        return result

    except Exception as e:
        return {"error": str(e)}
    
@app.get("/leads/{id}")
def get_lead(id: int):
    try:
        query = "SELECT * FROM leads WHERE id=%s"
        cursor.execute(query, (id,))
        result= cursor.fetchone()
            
        if result:
            return result
        else:
            return {"message":"Lead Not Found"}
        
    except Exception as e:
        return {"error":str(e)}

from schemas import LeadUpdate

@app.patch("/leads/{id}")
def update_lead(id: int, lead: LeadUpdate):
    try:
        update_fields = []
        values = []

        if lead.name is not None:
            update_fields.append("name = %s")
            values.append(lead.name)

        if lead.phone is not None:
            update_fields.append("phone = %s")
            values.append(lead.phone)

        if lead.email is not None:
            update_fields.append("email = %s")
            values.append(lead.email)

        if lead.budget is not None:
            update_fields.append("budget = %s")
            values.append(lead.budget)

        if lead.requirement is not None:
            update_fields.append("requirement = %s")
            values.append(lead.requirement)

        if lead.location is not None:
            update_fields.append("location = %s")
            values.append(lead.location)

        if lead.stage is not None:
            update_fields.append("stage = %s")
            values.append(lead.stage)

        if lead.loan_required is not None:
            update_fields.append("loan_required = %s")
            values.append(lead.loan_required)

        if not update_fields:
            return {"message": "No fields to update"}

        query = f"UPDATE leads SET {', '.join(update_fields)} WHERE id = %s"
        values.append(id)

        cursor.execute(query, tuple(values))
        db.commit()

        return {"message": "Lead updated successfully"}

    except Exception as e:
        return {"error": str(e)}
    
@app.delete("/leads/{id}")
def delete_lead(id: int):
    try:
        query = "DELETE FROM leads WHERE id = %s"
        cursor.execute (query, (id,))
        db.commit()
        
        if cursor.rowcount > 0:
            return {"message": "Lead deleted successfully"}
        else:
            return {"message":"Lead not found"}
        
    except Exception as e:
        return {"error": str(e)}