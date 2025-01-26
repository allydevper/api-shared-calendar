from fastapi import APIRouter, HTTPException
from typing import List
from models import Availability
from supabase_client import supabase

router = APIRouter()

@router.post("/availability/", response_model=Availability)
def create_availability(availability: Availability):
    try:
        event_dict = availability.model_dump(exclude={"id"})
        event_dict["start_date"] = event_dict["start_date"].isoformat()
        event_dict["end_date"] = event_dict["end_date"].isoformat()
        response = supabase.table("sc_availability").insert(event_dict).execute()
        if not response.data:
            raise HTTPException(status_code=response.status_code, detail="Error creating availability")
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/availability/", response_model=List[Availability])
def read_availability():
    try:
        response = supabase.table("sc_availability").select("*").execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="No availability records found")
        return response.data
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/availability/{availability_id}", response_model=Availability)
def read_availability_by_id(availability_id: str):
    try:
        response = supabase.table("sc_availability").select("*").eq("id", availability_id).execute()
        if not response.data or len(response.data) == 0:
            raise HTTPException(status_code=404, detail=f"Availability with ID {availability_id} not found")
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/availability/{availability_id}", response_model=Availability)
def update_availability(availability_id: str, updated_availability: Availability):
    try:
        response = supabase.table("sc_availability").update(updated_availability.model_dump()).eq("id", availability_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail=f"Availability with ID {availability_id} not found")
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/availability/{availability_id}")
def delete_availability(availability_id: str):
    try:
        response = supabase.table("sc_availability").delete().eq("id", availability_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail=f"Availability with ID {availability_id} not found")
        return {"detail": f"Availability with ID {availability_id} deleted"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/availability/participant/{participant_id}", response_model=List[Availability])
def read_availability_by_participant(participant_id: str):
    try:
        response = supabase.table("sc_availability").select("*").eq("participant_id", participant_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail=f"No availability records found for participant {participant_id}")
        return response.data
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 