from datetime import datetime
import json
import os
import sys
import time

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE_FILE = os.path.join(PROJECT_DIR, "process-state.json")
LOG_FILE = os.path.join(PROJECT_DIR, "process-stdout.log")
PID = os.getpid()

# process is already running/has not been terminated correctly
if os.path.exists(STATE_FILE):
    sys.exit()

with open(STATE_FILE, "w") as f:
    json.dump({"pid": PID}, f)

while True:
    with open(LOG_FILE, "a") as f:
        f.write(f"pid: {PID}, time: {datetime.utcnow()}\n")
    time.sleep(3)
