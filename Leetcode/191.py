'''
191. Number of 1 Bits


Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
'''

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        que=[]
        offset = 2
        while n!=0:
            if n%offset == 1:
                que.append(1)
            n=n//2
        return len(que)

if __name__ == '__main__':
    solution = Solution()
    t1=11
    print(solution.hammingWeight(t1))
