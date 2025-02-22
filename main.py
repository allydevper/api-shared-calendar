from fastapi import FastAPI
from user_controller import router as user_router
from event_controller import router as event_router
from participant_controller import router as participant_router
from availability_controller import router as availability_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://shared-calendar-production.up.railway.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(event_router)
app.include_router(participant_router)
app.include_router(availability_router)

@app.get("/")
def read_root():
    return {}
