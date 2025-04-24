import threading
import time

from threading import Thread, Event # Code to execute in an independent thread 
def countdown(n, started_evt): 
    print('countdown starting')
    started_evt.set()
    while n > 0: 
        print('T-minus', n, str(started_evt))
        n -= 1 
        time.sleep(5)
        # if n<8:
        #     started_evt.clear()

# Create the event object that will be used to signal startup
started_evt = Event()
# Launch the thread and pass the startup event 
print('Launching countdown') 
t = Thread(target=countdown, args=(10, started_evt))
print(f"hey {t.ident}")
t.start()
print(f"hey {t.ident}")
# Wait for the thread to start 
res = started_evt.wait(timeout=10)
print('countdown is running', res)






