from datetime import datetime
import os
import time

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(PROJECT_DIR, "process-stdout.log")

while True:
    with open(LOG_FILE, "a") as f:
        f.write(f"pid: {os.getpid()}, time: {datetime.utcnow()}\n")
    time.sleep(3)
