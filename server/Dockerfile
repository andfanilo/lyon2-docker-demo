FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:0.13.5 /uv /uvx /bin/

WORKDIR /app
COPY pyproject.toml uv.lock /app/
RUN uv sync --locked --no-install-project

COPY app.py app.py
# COPY model.joblib model.joblib

CMD ["uv", "run", "uvicorn", "--host", "0.0.0.0", "app:app"]
