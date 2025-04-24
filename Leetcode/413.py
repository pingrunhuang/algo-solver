# /usr/bin/python
# coding=utf-8

'''
413. Arithmetic Slices
A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.
'''


'''
This algorithm is not a good one though, the time complexity still get O(N2). I Think there could be a optimized way for 
choosing the start index so that the time complexity will drop to O(N)
'''
class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        self.A = A
        N =len(A)
        if N<3:
            return 0
        start_index=0
        end_index=start_index+2
        count=0
        while N-start_index>=3:
            # print(end_index)
            if end_index<N and self.isArithmeticSlice(start_index, end_index):
                count+=1
                end_index+=1
            else:
                # count += (end_index-start_index)*(end_index-start_index)/2
                start_index+=1
                end_index=start_index+2
        return count

    def isArithmeticSlice(self, startIndex, endIndex):
        for i in range(startIndex, endIndex-1):
            if self.A[i] - self.A[i+1] != self.A[i+1] - self.A[i+2]:
                return False
        return True
        

if __name__ == '__main__':
    solution = Solution()
    test_case1=[1, 2, 3, 4]
    print(solution.numberOfArithmeticSlices(test_case1))