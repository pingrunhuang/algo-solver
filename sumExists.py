
'''
This is an interview question asked by an interviewer in EA which I did not think it through during the interview in the situation where I don't have access to pen.
But later I figured it out when I got back to my computer and make a note on it.
Description:
given a target value, determine if the target array contains 2 integers that sum up to the target value  
'''
def isExists(arr, target):
    left_ptr = 0
    right_ptr = len(arr)-1
    while left_ptr < right_ptr:
        if arr[left_ptr]+arr[right_ptr]==target:
            return True
        if arr[left_ptr]+arr[right_ptr]<target:
            left_ptr+=1
        if arr[left_ptr]+arr[right_ptr]>target:
            right_ptr-=1
    return False


def twoSum(arr, target):
    from collections import defaultdict
    '''
    Another solution for this problem is by using hashmap to get O(n) to find out the index 
    '''
    if not arr or len(arr)<2:
        return (0,0)
    
    rest_dict=defaultdict()
    for index in range(len(arr)):
        if rest_dict.get(arr[index]) is not None:
            return (rest_dict.get(arr[index]),index)
        else:
            rest_dict[target-arr[index]] = index
    return (0,0)

if __name__ == "__main__":
    target=3
    t1 = [-19,-2,-2,5,14,25,36,47,58]
    print(isExists(t1, target))

    t2 = [2, 9, 11, 7]
    print(twoSum(t2, 9))