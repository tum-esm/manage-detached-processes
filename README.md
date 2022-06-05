# Manage Detached Processes

## What does it do?

Scenario: I want to start a background process from python and store the PID, so I can later terminate it. I do not want multiple processes running in parallel.

_This is just a demo project, to make this work on all operating systems._

## 🔌 How to run it?

Dependency management with poetry: https://python-poetry.org/docs/#installation

1. Set up the project interpreter

```bash
# create a virtual python environment
python3.9 -m venv .venv

# activate the virtual environment
source .venv/bin/activate

# install dependencies
poetry install
```

2. Manage process

```bash
# tries to start the process, stores the PID in
# "process-state.json", only starts the process
# if that state file does not exist
python src/start-process.py

# tries to end the process using the PID in
# "process-state.json", removes the state file
# if it exists
python src/end-process.py
```
