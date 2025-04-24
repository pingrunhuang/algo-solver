'''
In traditional DP problems with recursive algo, the time complexity is O(n^2).
The reason with this is because we calculate the fib(k) for redundent times
We should reuse the result that have been computed in the process
To do this, we can use a dictionary to store the result. 
'''

# fibonacci soluition with dictionary look up: bottom up
def fib1(n):
    result = {}
    for k in range(1,n+1):
        if k <= 2: 
            result[k] = 1
        else: 
            result[k] = result[k-1] + result[k-2]
    return result[n]

'''
The key to the dict way is that the dict will store each subproblems' result so that we don't need to count them again
time = #subproblems * (time per sub)
'''

if __name__ == '__main__':
    print(fib1(4))