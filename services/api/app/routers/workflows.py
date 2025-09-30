# services/api/app/routers/workflows.py

from fastapi import APIRouter
from pydantic import BaseModel

from services.flyte_workflows.workflows.train_workflow import train_wf

router = APIRouter()

class TrainReq(BaseModel):
    params: dict

@router.post("/train")
def run_train_workflow(req: TrainReq):
    run_id = train_wf(params=req.params)
    return {"mlflow_run_id": run_id}