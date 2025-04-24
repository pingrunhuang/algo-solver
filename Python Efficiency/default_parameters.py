class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=EvenStream()):
    # python function is evaluated once
    # therefore the stream will allways be the one obj that was initiated when the function is evaluated
    # calling function with the default parameter stream will be using the same obj
    for _ in range(n):
        print(stream.get_next())

if __name__=="__main__":
    print_from_stream(5)
    print_from_stream(7)