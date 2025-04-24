'''
We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.
'''

count=0
def merge(left, right, len_left, len_right):
    global count
    i = 0
    j = 0
    result = []
    while i<len_left and j<len_right:
        # inversion
        if left[i]>right[j]:
            result.append(right[j])
            j+=1
            # this is the key point: 
            count += len_right-j
        else:
            result.append(left[i])
            result.append(right[j])
            i+=1
            j+=1
    if i<len_left:
        result += left[i:]
        count+=len(left[i:])
    if j<len_right:
        result += right[j:]
    return result

def find_invension(arr):
    if len(arr) <= 1:
        return arr
    l = len(arr)
    mid = int(l/2)
    left = find_invension(arr[:mid])
    right = find_invension(arr[mid:])
    return merge(left,right, len(left), len(right))

if __name__=="__main__":
    test1= [2, 4, 1, 3, 5,-1]
    res = find_invension(test1)
    print(count)
    print(res)