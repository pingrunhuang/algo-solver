
"""
log(N^2)
"""

def swap(i1, i2, arr):
    temp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = temp

def bubbleSort(arr):
    n = len(arr)
    for i1 in range(0,n):
        for i2 in range(i1, n):
            if arr[i1]>arr[i2]:
                swap(i1,i2,arr)
    return arr

if __name__ == "__main__":
    t1=[6,2,1,5,7,9,4]
    print(bubbleSort(t1))