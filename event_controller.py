from fastapi import APIRouter, HTTPException
from typing import List
from models import Event
from supabase_client import supabase

router = APIRouter()

@router.post("/events/", response_model=Event)
def create_event(event: Event):
    try:
        response = supabase.table("sc_events").insert(event.model_dump()).execute()
        if not response.data:
            raise HTTPException(status_code=response.status_code, detail="Error creating event")
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/events/", response_model=List[Event])
def read_events():
    try:
        response = supabase.table("sc_events").select("*").execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="No events found")
        return response.data
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/events/{event_id}", response_model=Event)
def read_event(event_id: str):
    try:
        response = supabase.table("sc_events").select("*").eq("id", event_id).execute()
        if not response.data or len(response.data) == 0:
            raise HTTPException(status_code=404, detail=f"Event with ID {event_id} not found")
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/events/{event_id}", response_model=Event)
def update_event(event_id: str, updated_event: Event):
    try:
        response = supabase.table("sc_events").update(updated_event.model_dump()).eq("id", event_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail=f"Event with ID {event_id} not found")
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/events/{event_id}")
def delete_event(event_id: str):
    try:
        response = supabase.table("sc_events").delete().eq("id", event_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail=f"Event with ID {event_id} not found")
        return {"detail": f"Event with ID {event_id} deleted"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))