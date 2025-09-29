# services/api/app/ml/client.py

import mlflow
from mlflow.tracking import MlflowClient
import os

MLFLOW_URI = os.getenv("MLFLOW_TRACKING_URI", "http://mlflow:5000")
mlflow.set_tracking_uri(MLFLOW_URI)

class MLClient:
    def __init__(self):
        self.client = mlflow.tracking.MlflowClient()

    def create_experiment(self, name: str):
        try:
            return self.client.create_experiment(name)
        except:
            return self.client.get_experiment_by_name(name).experiment_id
        
    def create_run(self, exp_name: str, params: dict):
        exp = self.client.get_experiment_by_name(exp_name)
        exp_id = exp.experiment_id if exp is not None else self.create_experiment(exp_name)

        with mlflow.start_run(exp_id) as run:
            mlflow.log_params(params)
            mlflow.log_metric("dummy_metric", 0.9)
            return run.info