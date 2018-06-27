import time
from threading import Thread

answer = None

def check():
    time.sleep(2)
    if answer != None:
        return
    print('\nToo Slow, the enemy attacks you')
    exit()

Thread(target = check).start()
answer = input('Input something in 2 seconds >')
