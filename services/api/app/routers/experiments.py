# services/api/app/routers/experiments.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from services.api.app.ml.client import MLClient

router = APIRouter()
ml = MLClient()

class StartRunReq(BaseModel):
    experiment_name: str
    params: dict = {}

@router.post("/start")
def start_run(req: StartRunReq):
    try:
        run_info = ml.create_run(req.experiment_name, req.params)
        return {"run_id": run_info.run_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
