FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN pip install uv && uv sync

COPY src/ src/
COPY jobs/ jobs/

CMD ["python", "-m", "ml_jobs.worker.main"]