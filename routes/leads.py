from fastapi import APIRouter, Depends
# APIRouter → creates modular route groups
# Depends → used for Dependency Injection (DI)

from db import get_db
# Imports DB dependency function

from schemas import LeadCreate, LeadUpdate
# Pydantic schemas for request validation

from routes.lead_service import fetch_leads, create_lead_services, get_id, update_leads, delete_leads
# Service layer function for fetching leads


router = APIRouter()
# Router object containing all lead-related APIs



# ---------------- CREATE ----------------

@router.post("/lead")
# API Endpoint
# Creates POST API at /lead

def create_lead(
    lead: LeadCreate,
    # Request Body Validation using Pydantic schema

    db_tuple = Depends(get_db)
    # Dependency Injection
    # FastAPI injects conn + cursor
):

    conn, cursor = db_tuple
    # Unpacking injected dependency

    try:
        return create_lead_services(
            conn,
            cursor,
            lead
        )
    

    except Exception as e:
        # Error handling

        return {"error": str(e)}






# ---------------- GET ALL ----------------

@router.get("/leads")
# GET endpoint for fetching all leads

def get_leads(

    location: str = None,
    budget: str = None,
    stage: str = None,
    # Query Parameters
    # Example:
    # /leads?location=Indore

    db_tuple = Depends(get_db)
    # Dependency Injection

):

    conn, cursor = db_tuple
    # Unpacking conn + cursor

    try:

        return fetch_leads(
            cursor,
            location,
            budget,
            stage
        )

        # Service Layer Delegation
        # Route passes business logic to service layer

    except Exception as e:

        return {"error": str(e)}






# ---------------- GET ONE ----------------

@router.get("/leads/{id}")
# Dynamic Path Parameter Endpoint
# Example:
# /leads/5

def get_lead(

    id: int,
    # Path parameter validation

    db_tuple = Depends(get_db)

):

    conn, cursor = db_tuple

    try:
        return get_id()
    except Exception as e:
        return {"error":str(e)}







# ---------------- PATCH ----------------

@router.patch("/leads/{id}")
# PATCH endpoint
# Used for partial updates

def update_lead(

    id: int,

    lead: LeadUpdate,
    # Schema with optional fields

    db_tuple = Depends(get_db)

):

    conn, cursor = db_tuple

    try:
        return update_leads
    except Exception as e:

        return {"error": str(e)}








# ---------------- DELETE ----------------

@router.delete("/leads/{id}")
# DELETE endpoint

def delete_lead(

    id:int,

    db_tuple = Depends(get_db)

):

    conn, cursor = db_tuple

    try:
        return delete_leads

    except Exception as e:

        return {"error":str(e)}