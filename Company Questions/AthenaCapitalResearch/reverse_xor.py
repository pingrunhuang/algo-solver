"""
Reverse operations of XOR

For each element i of an array of non-negative integers, arr[n], is calculated as:
pref[i]=arr[i][]@arr[2][]@...@arr[i]
Here x @ y is the bitwise XOR of x and y. The array pref[n] contains the prefix XOR of all elements 
in arr[n] where 1 ≤ i≤ n.
Given the array pref, find the original array arr.
Note: There is always a unique arr for a given pref.

Example
n = 3
pref = [5, 2, 10]
• pref[1]= arr[1]= 5.
• pref[2]= arr[1] @ arr[2] = 5 @ 7 = 2.
• pref[3] = arr[1] @ arr[2] @ arr[3] = 5 @ 7 @ 8 = 10.
The original array arr is [5,7,8].
Function Description
Complete the function getOrigina/Array in the editor below.
getOriginalArray has the following parameter: int pref[n]: an array of integers
"""

def getOriginalArray(pref):
    n = len(pref)
    arr = [0]*n
    arr[0] = pref[0]
    for i in range(1, n):
        arr[i] = pref[i] ^ pref[i-1]
    return arr

pref = [5,2,10]
original = getOriginalArray(pref)
print(original)