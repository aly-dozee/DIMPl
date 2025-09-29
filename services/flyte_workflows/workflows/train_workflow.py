# flyte_workflows/workflows/train_workflows.py

from flytekit import workflow

from services.flyte_workflows.tasks.train_task import train_model

@workflow
def train_wf(params: dict) -> str:
    return train_model(params=params)