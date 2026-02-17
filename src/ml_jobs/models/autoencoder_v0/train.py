# src/ml_jobs/models/autoencoder_v0/train.py

import mlflow
import time

def main(latent_dim: int = 32, epochs: int = 3) -> None:
    mlflow.log_params("latent_dim", latent_dim)
    mlflow.log_params("epochs", epochs)

    for i in range(epochs):
        time.sleep(1)
        mlflow.log_metric("loss", 1.0 / (i + 1))