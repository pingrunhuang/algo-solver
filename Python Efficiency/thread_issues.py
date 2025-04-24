import requests
from threading import Thread
from queue import Queue
import time

# q = Queue(maxsize=20)
# def queue_page(page_num):
#     q.put(requests.get(f"https://some-website.com/page_{page_num}.html"))


# def compile(q:Queue):
#     if not q.full():
#         raise ValueError
#     else:
#         print(f"Done")
    
# threads = []
# for pnum in range(20):
#     t = Thread(target=queue_page, args=(pnum,))
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()

# compile(q)

class Sleepy(Thread):
    def run(self) -> None:
        print(f"Hello thread {self.ident}")
        time.sleep(5)
        print(f"World thread {self.ident}")

if __name__ == "__main__":
    threads = []
    for _ in range(5):
        t = Sleepy()
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print("finished")