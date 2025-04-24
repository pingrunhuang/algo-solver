'''Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
'''

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit_sum = 0
        pos = len(digits)-1
        for i in range(len(digits)-1,-1,-1):
            digit_sum+=10**(pos-i)*digits[i]
        return list(map(lambda x:int(x), str(digit_sum+1)))


if __name__ == '__main__':
    s = Solution()
    t1 = [1,2,3]
    print(s.plusOne(t1)) # [1,2,4]
    t2 = [4,3,2,1]
    print(s.plusOne(t2)) # [4,3,2,2]