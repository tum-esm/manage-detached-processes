from datetime import datetime
import time

print("Hello")

while True:
    print(datetime.utcnow())
    print("Wating 3 seconds")
    time.sleep(3)
