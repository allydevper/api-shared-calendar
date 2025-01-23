from fastapi import APIRouter

router = APIRouter()

@router.get("/user")
def get_user():
    return {"user_id": 1, "name": "John Doe", "email": "johndoe@example.com"}