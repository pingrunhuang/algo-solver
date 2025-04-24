"""
Given an array arr of n integers, 
make the array positive with the following operation: 
In one operation, select integers i (0 ≤ i < n) and x (-1018 ≤ x≤ 1018) and change arr[i] to x. 
An array is positive when the sum of each subarray of length greater than 1 is non-negative. 
More formally, after the operations, the following condition should hold for all values of l and r.
0<=l<r<n, sum(arr[i:r])>=0

Determine the minimum number of operations required to make the array positive

Example
arr = [2, 5, -8, -1, 2]
Assuming 0-based indexing, take i = 2 and x = 10.
The modified array is arr'= [2, 5, 10, -1, 2]. 
Now, every subarray of length greater than 1 has a non-negative sum. 
Return the number of operations 1.

Function Description
Complete the function getMinOperations in the editor below.
getMinOperations has the following parameter(s):
int arr[n]: an array of integers
"""

def getMinOperations(arr):
    n = len(arr)
    sum_so_far = 0
    count = 0

    for i in range(n):
        sum_so_far += arr[i]
        if sum_so_far < 0:
            count += 1
            min_value = float('inf')
            for j in range(i + 1, n):
                min_value = min(min_value, arr[j])
            sum_so_far += min_value - arr[i]

    return count

# Example usage:
arr = [2, 5, -8, -1, 2]
result = getMinOperations(arr)
print(result)  # Output: 1
