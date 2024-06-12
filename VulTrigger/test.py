import signal

# Handler function to be called on timeout
def handler(signum, frame):
    raise Exception("tttt")

# Function to apply the timeout to
def my_function():
    # Function logic here
    pass

# Setting the signal handler for the alarm signal
signal.signal(signal.SIGALRM, handler)

import time
import random
t1 = time.time()

while True:
    signal.alarm(3)  # Timeout in seconds
    try:
        print("start sleep", time.time() - t1)
        time.sleep(random.uniform(0, 6))
        print("sleep finish")
    except:
        print(time.time() - t1)
        continue

