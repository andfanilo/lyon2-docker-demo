FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:0.13.5 /uv /uvx /bin/

WORKDIR /app
COPY pyproject.toml uv.lock /app/
RUN uv sync --locked --no-install-project

COPY streamlit_app.py streamlit_app.py

CMD ["uv", "run", "streamlit", "run", "streamlit_app.py"]
