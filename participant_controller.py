from fastapi import APIRouter, HTTPException
from typing import List
from models import Participant
from supabase_client import supabase

router = APIRouter()

@router.post("/participants/", response_model=Participant)
def create_participant(participant: Participant):
    try:
        response = supabase.table("sc_participants").insert(participant.model_dump()).execute()
        if not response.data:
            raise HTTPException(status_code=response.status_code, detail="Error creating participant")
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/participants/", response_model=List[Participant])
def read_participants():
    try:
        response = supabase.table("sc_participants").select("*").execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="No participants found")
        return response.data
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/participants/{participant_id}", response_model=Participant)
def read_participant(participant_id: str):
    try:
        response = supabase.table("sc_participants").select("*").eq("id", participant_id).execute()
        if not response.data or len(response.data) == 0:
            raise HTTPException(status_code=404, detail=f"Participant with ID {participant_id} not found")
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/participants/{participant_id}", response_model=Participant)
def update_participant(participant_id: str, updated_participant: Participant):
    try:
        response = supabase.table("sc_participants").update(updated_participant.model_dump()).eq("id", participant_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail=f"Participant with ID {participant_id} not found")
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/participants/{participant_id}")
def delete_participant(participant_id: str):
    try:
        response = supabase.table("sc_participants").delete().eq("id", participant_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail=f"Participant with ID {participant_id} not found")
        return {"detail": f"Participant with ID {participant_id} deleted"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 