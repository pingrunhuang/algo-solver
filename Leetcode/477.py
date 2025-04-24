'''
477. Total Hamming Distance
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

Note:
Elements of the given array are in the range of 0 to 10^9
Length of the array will not exceed 10^4.

注意这种要遍历数组两次的题目，很多情况下是要考虑条件的，这样才能投机取巧，从而不会超时
'''

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # the method that exceed the time complexity
        #res = 0
        #for i1,v1 in enumerate(nums):
        #    for i2, v2 in enumerate(nums[i1+1:]):
        #        res += bin(v1^v2).count('1')
        #return res
        # since elements won't exceed 10^9 which is almost 2^32
        res=0
        n=len(nums)
        for i in range(33):
            bit_count = 0
            for num in nums:
                # calculate the number of bits
                bit_count+=(num>>i)&1
            res+=bit_count*(n-bit_count)
        return res
        

if __name__ == "__main__":
    solution = Solution()
    t1=[4,14,2]
    print(solution.totalHammingDistance(t1))