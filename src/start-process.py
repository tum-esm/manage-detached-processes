import os
import subprocess

import psutil

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INTERPRETER_PATH = os.path.join(PROJECT_DIR, ".venv", "bin", "python")
SCRIPT_PATH = os.path.join(PROJECT_DIR, "src", "process.py")


def process_is_running():
    for p in psutil.process_iter():
        try:
            arguments = p.cmdline()
            if (len(arguments) > 0) and (arguments[-1] == SCRIPT_PATH):
                return p.pid
        except (psutil.AccessDenied, psutil.ZombieProcess, psutil.NoSuchProcess):
            pass
    return None


existing_pid = process_is_running()
if existing_pid is not None:
    print(f"Background process already exists with PID {existing_pid}")
else:
    p = subprocess.Popen([INTERPRETER_PATH, SCRIPT_PATH], stderr=subprocess.PIPE)
    print(f"Started background process with PID {p.pid}")
