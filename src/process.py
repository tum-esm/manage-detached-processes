from datetime import datetime
import os
import sys
import time

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE_FILE = os.path.join(PROJECT_DIR, "process-state.json")
LOG_FILE = os.path.join(PROJECT_DIR, "process-stdout.log")

# process is already running/has not been terminated correctly
if os.path.exists(STATE_FILE):
    sys.exit()

while True:
    with open(LOG_FILE, "a") as f:
        f.write(f"pid: {os.getpid()}, time: {datetime.utcnow()}\n")
    time.sleep(3)
