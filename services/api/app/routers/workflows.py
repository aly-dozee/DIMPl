# services/api/app/routers/workflows.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
def ping():
    return {"message": "PING!"}