"""
Concurrency programming

make sure second() get executed after first(), third() get executed after second()
"""
from threading import Event

class Foo:
    def __init__(self):
        self.first_event = Event()
        self.second_event = Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_event.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        self.first_event.wait()
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_event.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        
        self.second_event.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()

def printFirst():
    print("first")
def printSecond():
    print("second")
def printThird():
    print("third")

if __name__ == "__main__":
    import threading

    threading._start_new_thread()
    foo = Foo()
    inputs = [1,3,2]
    threads = []
    for i in inputs:
        if i == 1:
            threads.append(threading.Thread(target=foo.first, name=i, kwargs={'printFirst':printFirst}))
        if i == 2:
            threads.append(threading.Thread(target=foo.second, name=i, kwargs={'printSecond':printSecond}))
        if i == 3:
            threads.append(threading.Thread(target=foo.third, name=i, kwargs={'printThird':printThird}))
    for t in threads:
        t.start()
    