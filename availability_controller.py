from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID
from models import Availability
from supabase_client import supabase

router = APIRouter()

@router.post("/availability/", response_model=Availability)
def create_availability(availability: Availability):
    response = supabase.table("sc_availability").insert(availability.model_dump()).execute()
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error creating availability")
    return response.data[0]

@router.get("/availability/", response_model=List[Availability])
def read_availability():
    response = supabase.table("sc_availability").select("*").execute()
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error reading availability")
    return response.data

@router.get("/availability/{availability_id}", response_model=Availability)
def read_availability_by_id(availability_id: UUID):
    response = supabase.table("sc_availability").select("*").eq("id", str(availability_id)).execute()
    if response.error or not response.data:
        raise HTTPException(status_code=404, detail="Availability not found")
    return response.data[0]

@router.put("/availability/{availability_id}", response_model=Availability)
def update_availability(availability_id: UUID, updated_availability: Availability):
    response = supabase.table("sc_availability").update(updated_availability.model_dump()).eq("id", str(availability_id)).execute()
    if response.status_code != 200 or not response.data:
        raise HTTPException(status_code=404, detail="Availability not found")
    return response.data[0]

@router.delete("/availability/{availability_id}")
def delete_availability(availability_id: UUID):
    response = supabase.table("sc_availability").delete().eq("id", str(availability_id)).execute()
    if response.status_code != 200 or not response.data:
        raise HTTPException(status_code=404, detail="Availability not found")
    return {"detail": "Availability deleted"} 