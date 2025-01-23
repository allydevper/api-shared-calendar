from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID
from models import Participant
from supabase_client import supabase

router = APIRouter()

@router.post("/participants/", response_model=Participant)
def create_participant(participant: Participant):
    response = supabase.table("sc_participants").insert(participant.model_dump()).execute()
    if not response.data:
        raise HTTPException(status_code=response.status_code, detail="Error creating participant")
    return response.data[0]

@router.get("/participants/", response_model=List[Participant])
def read_participants():
    response = supabase.table("sc_participants").select("*").execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="No participants found")
    return response.data

@router.get("/participants/{participant_id}", response_model=Participant)
def read_participant(participant_id: UUID):
    response = supabase.table("sc_participants").select("*").eq("id", str(participant_id)).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Participant not found")
    return response.data[0]

@router.put("/participants/{participant_id}", response_model=Participant)
def update_participant(participant_id: UUID, updated_participant: Participant):
    response = supabase.table("sc_participants").update(updated_participant.model_dump()).eq("id", str(participant_id)).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Participant not found")
    return response.data[0]

@router.delete("/participants/{participant_id}")
def delete_participant(participant_id: UUID):
    response = supabase.table("sc_participants").delete().eq("id", str(participant_id)).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Participant not found")
    return {"detail": "Participant deleted"} 