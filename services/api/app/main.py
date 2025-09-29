# /services/api/app/main.py

from fastapi import FastAPI

from services.api.app.routers import experiments, workflows

app = FastAPI(title="Dozee Data & Infrastructure Management Platform (DIMPl) API")

app.include_router(experiments.router, prefix="/experiments", tags=["experiments"])
app.include_router(workflows.router, prefix="/workflows", tags=["workflows"])