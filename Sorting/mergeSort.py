from collections import deque

"""
complexity: O(nlog(n))
divide and conquer algo
"""
def merge(lList, rList):
    '''
    Return a merged list
    '''
    result=[]
    left_list=deque(lList)
    right_list=deque(rList)
    while len(left_list)!=0 and len(right_list)!=0:
        '''
        Wrong idea here is trying to pop the first element at first, some element on the right will be missing
        left_ele=left_list.popleft()
        right_ele = right_list.popleft()
        '''
        if left_list[0]>right_list[0]:
            result.append(left_list.popleft())
        else:
            result.append(right_list.popleft())
    while len(left_list)!=0:
        result.append(left_list.popleft())
    while len(right_list)!=0:
        result.append(right_list.popleft())
    return result

def mergeSort(l):
    if len(l)<=1:
        return l
    n=len(l)
    middle_index = int(n/2)
    # devide part: devide each sub array into sorted array
    left_halve = mergeSort(l[:middle_index])
    right_halve = mergeSort(l[middle_index:])
    return merge(left_halve, right_halve)

if __name__=='__main__':
    test_case1=[12, 11, 13, 5, 6, 7]
    print(mergeSort(test_case1))