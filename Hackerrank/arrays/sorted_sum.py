def f(cur_val:int, sorted_arr:list, prev_fn:int):
    """
    f(n) = f(n-1) + rank*cur_val + sum(sorted_arr[rank:])
    """
    i = 0
    j = len(sorted_arr)
    rank = j
    while i<j:
        rank = (i+j)//2
        if sorted_arr[rank] > cur_val:
            j = rank-1
        elif sorted_arr[rank] < cur_val:
            i = rank+1
        else:
            break
    sorted_arr.insert(rank, cur_val)
    return prev_fn+rank*cur_val+sum(sorted_arr[rank:])

def sortedSum(a):
    n = len(a)
    result = a[0]
    sorted_arr = [a[0]]
    prev_fn = a[0]
    for val in a[1:]:
        print(prev_fn, sorted_arr)
        prev_fn = f(val, sorted_arr, prev_fn)
        result += prev_fn
    
    return result



if __name__=="__main__":
    test_case = [9,5,8]
    assert sortedSum(test_case)==80%(10**9+7)