import sys
import os
from time import sleep

i = int(input("enter minutes: "))
seconds = i * 60

try:
    if i > 0:
        print("Sleeping For {} minutes.".format(i))
        sleep(seconds)
    print("wake up")
    for i in range(5):
        print(chr(7)),
        sleep(1)
    else:
        os.system("aplay alarm.wav&")  # only for linux
except KeyboardInterrupt:
    print("Interrupted by user")
    sys.exit(1)
