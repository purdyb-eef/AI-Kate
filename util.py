import time
import sys

def delayPrint(str):
    for c in str:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.075)

def pause(sec):
    time.sleep(sec)
