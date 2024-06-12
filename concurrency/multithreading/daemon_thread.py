# Daemon threads

from threading import Thread
import time

DELAY = 1

def show_timer():
    count = 0
    while(True):
        count += 1
        time.sleep(DELAY)
        print(f"Has been waiting for {count} seconds(s)...")


thread = Thread(target=show_timer, daemon=True)
thread.start()

answer = input("Do you want to exit?\n")
