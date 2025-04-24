
'''
a - 1
b - 2
...
z - 24
given a number, return how many possible ways to decode it
'''
from functools import wraps
import time

def timmer(func):
    @wraps(func)
    def clock(*args, **wargs):
        start = time.clock()
        print(func(*args, **wargs))
        end = time.clock()
        print("Time duration of ", func.__name__, " is ", end-start)
    return clock

@timmer
def decodeRecursion(num):
    '''
    Devide and conquer
    '''
    def helper(num,l):
        """
        @param num the number represented encoded string
        @param l the length of the rest of the string
        """
        if l == 0:
            return 1
        s = len(num) - l
        if num[s]=="0":
            return 0
        result = helper(num, l-1)
        if l >=2 and int(num[s:s+2])<=26:
            result += helper(num, l-2)
        return result

    return helper(num, len(num))

@timmer
def decodeMemo(num):
    """
    Since there are a lot of unnecessary repeation, we can bypass them with a memo
    The memo's index represent the length of the current substring and the value is the number of ways to decode it
    """
    memo = [None for _ in range(len(num)+1)]
    def helper(num, l, mem):
        # initialize
        if l == 0:
            return 1
        s = len(num) - l
        if num[s]=="0":
            return 0
        if mem[l]:
            return mem[l]
        result = helper(num, l-1, mem)
        if l >= 2 and int(num[s:s+2])<=26:
            result += helper(num, l-2, mem)
        # remember the state
        mem[l] = result
        return result
    return helper(num, len(num), memo)




if __name__ == "__main__":
    test_case1="1213213213123423412424132422"
    test_case2="12345"
    test_case3="011"
    test_case4="2789"
    print(decodeRecursion(test_case1))
    print(decodeRecursion(test_case2))
    print(decodeRecursion(test_case3))
    print(decodeRecursion(test_case4))


    print(decodeMemo(test_case1))
    print(decodeMemo(test_case2))
    print(decodeMemo(test_case3))
    print(decodeMemo(test_case4))