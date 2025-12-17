# services/api/app/routers/ml_upload.py

from fastapi import APIRouter, UploadFile, Form
from services.api.app.ml.uploader import save_and_extract_tarball

router = APIRouter()

@router.post
def upload_tarball(run_id: str = Form(...), file: UploadFile = None):
    if not file:
        return {"error": "No file uploaded"}
    
    path = save_and_extract_tarball(file, run_id)
    return {"status": "ok", "saved_to": path}