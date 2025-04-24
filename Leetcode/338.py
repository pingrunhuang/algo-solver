# /usr/bin/python
# coding=utf-8

'''
338. Counting Bits
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

1. space complexity=O(n)
2. time complexity=O(n)

'''

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = []
        one_bit_checkpoint = 2
        for i in range(num+1):
            if i == 0:
                result.append(0)
            elif i == 1:
                result.append(1)
            elif i == 2:
                result.append(1)
            elif i == one_bit_checkpoint<<1:
                result.append(1)
                one_bit_checkpoint = one_bit_checkpoint<<1
            else:
                result.append(result[one_bit_checkpoint] + result[i-one_bit_checkpoint])


        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.countBits(17))