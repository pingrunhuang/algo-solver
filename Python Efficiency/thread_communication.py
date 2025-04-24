from queue import Queue
from threading import Thread
import time
import random


def data_generation():
    return random.random()


def producer(q:Queue):
    while True:
        try:
            data = data_generation()
            print(f"generated data: {data}")
            q.put(data)
            seconds = 2
            print(f"sleeping for {seconds}")
            time.sleep(seconds)
            print("wake up")
        except KeyboardInterrupt:
            break


def consumer(q:Queue):
    while True:
        try:
            data = q.get()
            print(f"consuming data: {data}")
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    q = Queue()
    t1 = Thread(target=producer, args=(q,))
    t2 = Thread(target=consumer, args=(q,))
    t1.start()
    t2.start()
