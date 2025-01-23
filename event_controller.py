from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID
from models import Event
from supabase_client import supabase

router = APIRouter()

@router.post("/events/", response_model=Event)
def create_event(event: Event):
    response = supabase.table("sc_events").insert(event.model_dump()).execute()
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error creating event")
    return response.data[0]

@router.get("/events/", response_model=List[Event])
def read_events():
    response = supabase.table("sc_events").select("*").execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="No events found")
    return response.data

@router.get("/events/{event_id}", response_model=Event)
def read_event(event_id: UUID):
    response = supabase.table("sc_events").select("*").eq("id", str(event_id)).execute()
    if response.error or not response.data:
        raise HTTPException(status_code=404, detail="Event not found")
    return response.data[0]

@router.put("/events/{event_id}", response_model=Event)
def update_event(event_id: UUID, updated_event: Event):
    response = supabase.table("sc_events").update(updated_event.model_dump()).eq("id", str(event_id)).execute()
    if response.status_code != 200 or not response.data:
        raise HTTPException(status_code=404, detail="Event not found")
    return response.data[0]

@router.delete("/events/{event_id}")
def delete_event(event_id: UUID):
    response = supabase.table("sc_events").delete().eq("id", str(event_id)).execute()
    if response.status_code != 200 or not response.data:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"detail": "Event deleted"} 