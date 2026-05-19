from fastapi import FastAPI
# Importing FastAPI class
# Used to create the main FastAPI application object

from routes.auth import router as auth_router

from routes.leads import router as leads_router
# Importing router object from routes/leads.py
# "as leads_router" creates an alias name
# Router contains all lead-related API endpoints


app = FastAPI()
# Creating main FastAPI application instance
# This is the core app object that runs the backend server


app.include_router(leads_router)
# Registers/includes all routes from leads_router into main app
# Connects routes file to main application
# Without this, API endpoints will not work

app.include_router(auth_router)