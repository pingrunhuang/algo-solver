import threading

def printFoo():
    print("foo", end="")

def printBar():
    print("bar", end="")

def semaphore_solution(n=10):
    class FooBar:
        def __init__(self, n):
            self.n = n
            self.semFoo = threading.Semaphore(1)
            self.semBar = threading.Semaphore(0)

        def foo(self, printFoo: 'Callable[[], None]') -> None:
            for i in range(self.n):
                self.semFoo.acquire()
                # printFoo() outputs "foo". Do not change or remove this line.
                printFoo()
                self.semBar.release()

        def bar(self, printBar: 'Callable[[], None]') -> None:
            for i in range(self.n):
                self.semBar.acquire()
                # printBar() outputs "bar". Do not change or remove this line.
                printBar()
                self.semFoo.release()

    fooBar = FooBar(n)
    
    t1 = threading.Thread(target=fooBar.foo, args=(printFoo,))
    t2 = threading.Thread(target=fooBar.bar, args=(printBar,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

def lock_solution(n=10):
    """
    similar to the semaphore solution 
    """
    class FooBar:
        def __init__(self, n):
            self.n = n
            self.lock1 = threading.Lock()
            self.lock2 = threading.Lock()
            self.lock2.acquire()

        def foo(self, printFoo: 'Callable[[], None]') -> None:
            for i in range(self.n):
                self.lock1.acquire()
                # printFoo() outputs "foo". Do not change or remove this line.
                printFoo()
                self.lock2.release()

        def bar(self, printBar: 'Callable[[], None]') -> None:
            for i in range(self.n):
                self.lock2.acquire()
                # printBar() outputs "bar". Do not change or remove this line.
                printBar()
                self.lock1.release()

    fooBar = FooBar(n)
    t1 = threading.Thread(target=fooBar.foo, args=(printFoo,))
    t2 = threading.Thread(target=fooBar.bar, args=(printBar,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


def barrier_solution(n=10):
    """
    barrier is not so certain where to put the wait() method
    """
    class FooBar:
        def __init__(self, n):
            self.n = n
            # when they all call the wait() method, the barrier is awoken
            self.barrier = threading.Barrier(2)

        def foo(self, printFoo: 'Callable[[], None]') -> None:
            for i in range(self.n):
                # printFoo() outputs "foo". Do not change or remove this line.
                printFoo()
                self.barrier.wait()

        def bar(self, printBar: 'Callable[[], None]') -> None:
            for i in range(self.n):
                # printBar() outputs "bar". Do not change or remove this line.
                self.barrier.wait()
                printBar()

    fooBar = FooBar(n)
    t1 = threading.Thread(target=fooBar.foo, args=(printFoo,))
    t2 = threading.Thread(target=fooBar.bar, args=(printBar,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

def condition_solution(n=10):
    class FooBar:
        def __init__(self, n):
            self.n = n
            self.condition = threading.Condition()
            self.isFooLocked = False

        def foo(self, printFoo: 'Callable[[], None]') -> None:
            for i in range(self.n):
                with self.condition:
                    self.condition.wait_for(lambda : not self.isFooLocked)
                    
                    self.isFooLocked = True
                    # printFoo() outputs "foo". Do not change or remove this line.
                    printFoo()
                    self.condition.notify()

        def bar(self, printBar: 'Callable[[], None]') -> None:
            for i in range(self.n):
                with self.condition:
                    self.condition.wait_for(lambda : self.isFooLocked)
                    # printBar() outputs "bar". Do not change or remove this line.
                    printBar()
                    self.isFooLocked = False
                    self.condition.notify()

    fooBar = FooBar(n)
    t1 = threading.Thread(target=fooBar.foo, args=(printFoo,))
    t2 = threading.Thread(target=fooBar.bar, args=(printBar,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

def event_solution(n=10):
    class FooBar:
        def __init__(self, n):
            self.n = n
            self.condition = threading.Event()
            self.isFooLocked = False

        def foo(self, printFoo: 'Callable[[], None]') -> None:
            for i in range(self.n):
                with self.condition:
                    self.condition.wait_for(lambda : not self.isFooLocked)
                    
                    self.isFooLocked = True
                    # printFoo() outputs "foo". Do not change or remove this line.
                    printFoo()
                    self.condition.notify()

        def bar(self, printBar: 'Callable[[], None]') -> None:
            for i in range(self.n):
                with self.condition:
                    self.condition.wait_for(lambda : self.isFooLocked)
                    # printBar() outputs "bar". Do not change or remove this line.
                    printBar()
                    self.isFooLocked = False
                    self.condition.notify()

    fooBar = FooBar(n)
    t1 = threading.Thread(target=fooBar.foo, args=(printFoo,))
    t2 = threading.Thread(target=fooBar.bar, args=(printBar,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()



if __name__ == "__main__":
    barrier_solution()

