

'''
find how many combinations that sum up to a given total
None negative elements
'''

def rec(arr, total, last_index):
    '''
    Recursive function that add up to a given total
    '''
    if total==0:
        return 1
    elif total < 0:
        return 0
    elif last_index<0:
        return 0
    return rec(arr, total - arr[last_index], last_index-1) + rec(arr, total, last_index-1)

def count_sets(arr, total):
    return rec(arr, total, len(arr)-1)

def dp(arr, total, last_index, mem):
    key = str(total) + ":" + str(last_index)
    if mem.get(key):
        return mem.get(key)
    elif total==0:
        return 1
    elif last_index<0:
        return 0
    elif total < arr[last_index]:
        temp_result = dp(arr, total, last_index-1, mem)
    else:
        temp_result = dp(arr, total-arr[last_index], last_index-1, mem) + dp(arr, total, last_index-1, mem)
    mem.update({key:temp_result})
    return temp_result

def count_sets_dp(arr, total):
    mem = {}
    # passing a memory for memoization 
    return dp(arr, total, len(arr)-1, mem)

if __name__ == "__main__":
    result = count_sets_dp([2,4,6,10], 16)
    print(result)