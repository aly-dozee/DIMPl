# DIMPl (Data Infrastructure Management Platform)

## Installation

TBA

## Usage

TBA

## Start Commands

- **Starting the API:**
uv run -m uvicorn services.api.app.main:app --reload

- **Starting MLFlow:**
uv run mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host 0.0.0.0 --port 5000
