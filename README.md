# Docker Demo

```powershell
# ---- Command line ----
pwd
cd ..
mkdir C:\workspace
cd C:\workspace
ls

# ---- Git ----
git clone https://github.com/andfanilo/lyon2-docker-demo
cd lyon2-docker-demo
code .
git log --oneline

# ---- Edit code, git revert ----
git diff
git commit -am "Say Bonjour"
git revert --no-edit HEAD
git log --oneline

# ---- uv ----
cd td
uv run app.py
uv add requests
git diff
git restore .

# ---- Docker: containers ----
docker run hello-world
docker run -it --rm python:3.12-slim python
docker images
docker ps -a

# ---- Docker: build and compose ----
docker build -t td-lyon2 .
docker run --rm td-lyon2
cd ..
docker compose up --build -d
# http://localhost:8501
# http://localhost:8000/docs
docker compose exec server python -c "print(2 + 3)"

# ---- Claude ----
claude
> Explain how this project works: what runs in each folder, and how client, server and MongoDB talk to each other
> In docker-compose.yml, enable Streamlit's agent API on the client service with the STREAMLIT_SERVER_ENABLE_AGENT_API environment variable
/exit
docker compose up -d
claude mcp add --transport http iris-app http://localhost:8501/_stcore/agent/mcp
claude
> Use iris-app: set sepal length 5, sepal width 3, petal length 1, petal width 0, press Predict flower and tell me what the app shows
/exit
docker compose down
```
