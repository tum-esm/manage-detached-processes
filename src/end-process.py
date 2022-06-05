import json
import os
import psutil

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE_FILE = os.path.join(PROJECT_DIR, "process-state.json")

if not os.path.isfile(STATE_FILE):
    print("No background process found")
else:
    try:
        with open(STATE_FILE, "r") as f:
            pid = json.load(f)["pid"]
        try:
            psutil.Process(pid).terminate()
            print(f"Terminated background process with PID {pid}")
        except psutil.NoSuchProcess:
            print("Process has already been terminated")
        os.remove(STATE_FILE)
    except Exception as e:
        print(f"Could not terminate background process: {e}")
