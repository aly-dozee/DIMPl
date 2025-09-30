# flyte_workflows/tasks/train_task.py

from flytekit import task
import mlflow
import os

mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI", "http://127.0.0.1:5000"))

@task
def train_model(params: dict) -> str:
    with mlflow.start_run() as run:
        mlflow.log_params(params)
        mlflow.log_metric("val_accuracy", 0.9)
        return run.info.run_id