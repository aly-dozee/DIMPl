# src/ml_jobs/worker/runner.py

from __future__ import annotations

import importlib
import mlflow
import traceback
from typing import Any

def run_job(job: dict[str, Any]) -> None:
    mlflow.start_run(run_name=job["job_id"])
    try:
        module_name ,fn_name = job["entrypoint"].split(":")
        module = importlib.import_module(module_name)
        fn = getattr(module, fn_name)

        fn(**job.get("params", {}))

        mlflow.log_param("status", "success")
    except Exception:
        mlflow.log_param("status", "failed")
        mlflow.log_text(traceback.format_exc(), "error.txt")
        raise
    finally:
        mlflow.end_run()