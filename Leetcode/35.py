class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return 0
        result = 0
        low = 0
        high = len(nums)-1
        while low < high:
            mid = low + (high-low)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                result = mid
                high = mid
            else:
                result = mid+1
                low = mid +1
        if low == len(nums)-1 and target>nums[low]:
            return len(nums)
        return result


if __name__ == "__main__":
    s = Solution()
    t1 = [1,3,5,6]
    assert s.searchInsert(t1, 5) == 2

    t2 =  [1,3,5,6]
    assert s.searchInsert(t2, 2) == 1

    t3 = [1,3,5,6]
    assert s.searchInsert(t3, 7) == 4

    t4 = [1,3,5,6]
    assert s.searchInsert(t4, 0) == 0

    t5 = [1]
    assert s.searchInsert(t5, 0) == 0