from schemas import LeadCreate

@app.post("/lead")
def create_lead(lead: LeadCreate):
    return {
        "message": "Lead Received",
        "data": lead
    }