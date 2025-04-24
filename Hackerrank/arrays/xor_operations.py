"""
For each element i of an array of non-negative integers, arr[n] is calculated as
pref[i] = arr[1][] XOR arr[2][] XOR ... XOR arr[i]

here XOR denotes bit wise XOR operation of x and y
the array pref[n] contains the prefix XOR of all elements in arr[n] where 1 <=i<=n
given the array pref, find the original array arr
"""

def getOriginalArray(pref:list)->list:
    n = len(pref)
    if n == 1:
        return pref
    if n == 2:
        return pref + [pref[1]^arr[0]]
    arr = [None]*n
    arr[0] = pref[0]
    arr[1] = pref[1]^arr[0]
    cum_xor = arr[1]^arr[0]
    for i in range(2, n):
        arr[i] = pref[i]^cum_xor
        cum_xor = cum_xor^arr[i]
    print(arr)
    return arr
if __name__=="__main__":
    test = [5,2,10]
    result = getOriginalArray(test)
    