
"""
Given a list of non negative integers, arrange them such that they form the largest number.

# TODO
"""

class NewComparableNum(str):
    # Sorting is only performed with < operator. commenting the __lt__ operator leads to TypeError: unorderable types
    def __lt__(self, other):

        return self + other > other + self
    
class Solution:
    def largestNumber(self, nums):
        new_nums = [NewComparableNum(x) for x in nums]
        # question: which entry should be considered larger?
        new_nums = sorted(new_nums)
        print(new_nums)
        return "0" if new_nums[0] == "0" else "".join(new_nums)

def test1():
    nums = [3,30,34,5,9]
    s = Solution()
    assert s.largestNumber(nums) == "9534330"

def test2():
    nums = [321,123]
    s = Solution()
    assert s.largestNumber(nums) == "321123"

def test3():
    nums = [121,12]
    s = Solution()
    assert s.largestNumber(nums) == "12121"

if __name__ == '__main__':
    test3()
    