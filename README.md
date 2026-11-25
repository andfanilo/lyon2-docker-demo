# Docker Demo

Live demo of the developer toolbox, step by step: command line, Git, uv, Docker and an AI coding assistant.

```
lyon2-docker-demo
├── td/                  <- Hello World script, 1 uv project, 1 Docker image
├── client/              <- Streamlit frontend, 1 uv project, 1 Docker image
├── server/              <- FastAPI backend, 1 uv project, 1 Docker image
└── docker-compose.yml   <- Runs client + server + MongoDB together
```

Each of `td`, `client` and `server` contains:

- `pyproject.toml`: the dependencies we asked for
- `uv.lock`: the exact versions installed, so everyone gets the same environment
- `.python-version`: the Python version (3.12)
- `Dockerfile`: how to build the image, using uv instead of `pip install -r requirements.txt`
- `.dockerignore`: keeps the local `.venv` out of the image

Commands below use Git Bash. In PowerShell, replace `$(pwd)` with `${PWD}`.

## 1. Command line

```bash
pwd                          # Where am I?
ls                           # What's in this folder? (dir in the Windows prompt)
mkdir -p /c/workspace        # Create a folder (C:\workspace)
cd /c/workspace              # Move into it. Press Tab to autocomplete folder names
cd ..                        # Go up one folder
cd -                         # Go back to the previous folder
code .                       # Open the current folder in VS Code
```

## 2. Git

```bash
git --version

# Download the project and its full history
cd /c/workspace
git clone https://github.com/andfanilo/lyon2-docker-demo
cd lyon2-docker-demo

git log --oneline            # History of commits, newest first
git status                   # What changed since the last commit?
```

## 3. Edit code, then undo with Git

```bash
# Edit td/app.py in VS Code, for example change "Hello" to "Bonjour"
git status                   # app.py is "modified"
git diff                     # Line by line: red is removed, green is added

# Undo an edit you have NOT committed yet
git restore td/app.py

# Undo an edit you HAVE committed
git add td/app.py
git commit -m "Say Bonjour"
git log --oneline
git revert --no-edit HEAD    # New commit that cancels the last one. History is kept
git log --oneline
```

## 4. uv: run the Python projects locally

```bash
uv --version
uv python list               # Python versions uv knows about. No python.org download needed

# Run the td script. The first uv run creates .venv and installs packages from uv.lock
cd td
uv run app.py
uv add requests              # Add a dependency: updates pyproject.toml and uv.lock
uv remove requests           # ...and remove it

# Run the FastAPI server: http://localhost:8000/docs (Ctrl+C to stop)
# /add and /list need MongoDB, start it with: docker run -d -p 27017:27017 mongo
cd ../server
uv run uvicorn --reload app:app

# Run the Streamlit client: http://localhost:8501 (Ctrl+C to stop)
# The Predict button calls http://server:8000, a name that only exists in docker compose
cd ../client
uv run streamlit run streamlit_app.py

# Run a tool without adding it to the project
uvx ruff check
```

## 5. Docker

```bash
docker version
docker compose version

# First image: download it, run it, look at what's left
docker pull hello-world
docker run hello-world
docker images                # Images on your machine
docker ps                    # Running containers
docker ps -a                 # All containers, including stopped ones
docker rm <container id>     # Delete a stopped container

# Run Python code without installing Python. Browse more images on https://hub.docker.com/
docker pull python:3.12-slim
docker run --rm python:3.12-slim python -c "print(2 + 3)"     # One command, then delete the container
docker run -it --rm python:3.12-slim python                    # Interactive Python shell, exit() to quit

# exec: run a command inside a container that is already running
docker run -d --name py-demo python:3.12-slim sleep infinity   # -d: run in the background
docker exec py-demo python -c "import platform; print(platform.platform())"
docker exec -it py-demo bash                                   # Open a shell inside, exit to quit
docker rm -f py-demo                                           # Stop and delete it

# Mount your current folder into a Jupyter container (big image, long download)
MSYS_NO_PATHCONV=1 docker run -v "$(pwd)":/tmp/working -w=/tmp/working --rm -it -p 8888:8888 kaggle/python jupyter notebook --no-browser --ip=0.0.0.0 --allow-root --NotebookApp.token="" --notebook-dir=/tmp/working

# Build and run our own images. Open td/Dockerfile first
cd td
docker build -t td-lyon2 .   # -t: image name. ".": folder that contains the Dockerfile
docker run --rm td-lyon2

cd ../client
docker build -t mlops-client:latest .
docker run -p 8501:8501 --rm mlops-client:latest   # -p host port:container port

cd ../server
docker build -t mlops-server:latest .
docker run -p 8000:8000 --rm mlops-server:latest

# Run client + server + MongoDB together. Open docker-compose.yml first
cd ..
docker compose up --build    # http://localhost:8501, then Predict flower. Ctrl+C to stop
docker compose exec server uv run python -c "import sys; print(sys.version)"   # From another terminal
docker compose down          # Delete the containers
```

## 6. AI coding assistant

Same idea for [Claude Code](https://docs.claude.com/en/docs/claude-code/overview) (`claude`), [GitHub Copilot CLI](https://github.com/features/copilot/cli) (`copilot`) and [Gemini CLI](https://github.com/google-gemini/gemini-cli) (`gemini`): start it from the project folder, and it reads and edits files, then runs commands after you approve them.

```bash
cd /c/workspace/lyon2-docker-demo
claude                       # or: copilot, or: gemini
```

Prompts to try, one at a time:

```text
> Explain the architecture of this project and how client, server and MongoDB talk to each other
> Add a GET /health endpoint to server/app.py that returns {"status": "ok"}, then run the server with uv and test it
> In docker-compose.yml, enable Streamlit's agent API on the client service with the STREAMLIT_SERVER_ENABLE_AGENT_API environment variable
```

Review what it did, like a colleague's work:

```bash
git status
git diff
git restore .                # Don't like it? Throw it all away
```

### Let the agent use the Streamlit app through MCP

With the agent API on, Streamlit serves an MCP server at `/_stcore/agent/mcp`: the agent fills the form and presses buttons like a browser user would.

```bash
docker compose up --build -d   # Restart with the new environment variable

# Register the app's MCP server, then restart the assistant
claude mcp add --transport http iris-app http://localhost:8501/_stcore/agent/mcp
copilot mcp add --transport http iris-app http://localhost:8501/_stcore/agent/mcp
gemini mcp add --transport http iris-app http://localhost:8501/_stcore/agent/mcp
```

```text
> Use the iris-app MCP server: set sepal length 5, sepal width 3, petal length 1, petal width 0, press Predict flower and tell me what the app displays
> Why is there no flower name in the answer? Complete server/train.py so /predict returns one
```

```bash
docker compose down
```
