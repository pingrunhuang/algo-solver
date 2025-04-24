class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num_str = str(n)
        numbers = set([n])
        while True:
            temp_num = 0
            for x in num_str:
                temp_num += (int(x) ** 2)

            if temp_num == 1:
                return True
            if temp_num in numbers:
                return False
            numbers.add(temp_num)
            num_str = str(temp_num)

if __name__ == "__main__":
    s = Solution()
    t = 19
    print(s.isHappy(t))
    t = 7
    print(s.isHappy(t))
    t = 1
    print(s.isHappy(t))
