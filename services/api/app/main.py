# /services/api/app/main.py

from fastapi import FastAPI

from services.api.app.routers import experiments, ml_upload, workflows

app = FastAPI(title="Dozee Data & Infrastructure Management Platform (DIMPl) API")

app.include_router(experiments.router, prefix="/experiments", tags=["experiments"])
app.include_router(workflows.router, prefix="/workflows", tags=["workflows"])
app.include_router(ml_upload.router, prefix="/ml", tags=["ml"])

@app.get("/")
def root():
    return {"msg": "Welcome to DIMPl!"}

@app.get("/health")
def health():
    return {"status": "OK"}