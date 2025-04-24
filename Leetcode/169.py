class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        counter = {}
        threshold = len(nums)//2
        for x in nums:
            if counter.get(x):
                counter[x] += 1
            else:
                counter[x] = 1
            if counter[x] > threshold:
                    return x
        


if __name__ == "__main__":
    s = Solution()
    t = [3,2,3]
    assert s.majorityElement(t) == 3 
    t = [2,2,1,1,1,2,2]
    assert s.majorityElement(t) == 2
    t = [1]
    assert s.majorityElement(t) == 1
