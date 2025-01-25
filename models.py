from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

class Event(BaseModel):
    id: Optional[str] = None
    name: str
    description: Optional[str]
    admin_id: Optional[str] = None

class Participant(BaseModel):
    id: Optional[str]
    event_id: str
    name: str
    email: Optional[str]
    created_at: Optional[datetime]

class Availability(BaseModel):
    id: Optional[str]
    participant_id: str
    event_id: str
    start_date: date
    end_date: date
    created_at: Optional[datetime] 