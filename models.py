from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime, date

class Event(BaseModel):
    id: Optional[UUID]
    name: str
    description: Optional[str]
    admin_id: Optional[UUID]
    created_at: Optional[datetime]

class Participant(BaseModel):
    id: Optional[UUID]
    event_id: UUID
    name: str
    email: Optional[str]
    created_at: Optional[datetime]

class Availability(BaseModel):
    id: Optional[UUID]
    participant_id: UUID
    event_id: UUID
    start_date: date
    end_date: date
    created_at: Optional[datetime] 