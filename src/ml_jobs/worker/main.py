# src/ml_jobs/worker/main.py

import json
from redis import Redis
from rq import Queue

from ml_jobs.worker.runner import run_job

def main() -> None:
    redis = Redis(host="localhost", port=6379)
    q = Queue("training", connection="redis")

    job = json.load(open("jobs/autoencoder_debug.json"))
    q.enqueue(run_job, job)

if __name__ == "__main__":
    main()