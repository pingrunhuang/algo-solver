"""
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""
import sched
import time

scheduler = sched.scheduler(timefunc=time.time, delayfunc=time.sleep)

def scheduling(n):
    def my_func(name, start):
        now = time.time()
        elapsed = int(now-start)
        print("")


if __name__ == "__main__":
    for x in range(4):
        print(x)