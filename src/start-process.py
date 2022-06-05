import os
import subprocess

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE_FILE = os.path.join(PROJECT_DIR, "process-state.json")

INTERPRETER_PATH = os.path.join(PROJECT_DIR, ".venv", "bin", "python")
SCRIPT_PATH = os.path.join(PROJECT_DIR, "src", "process.py")

if os.path.isfile(STATE_FILE):
    print("Background process already exists")
else:
    p = subprocess.Popen([INTERPRETER_PATH, SCRIPT_PATH], stderr=subprocess.PIPE)
    print(f"Started background process with PID {p.pid}")
