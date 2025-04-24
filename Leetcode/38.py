class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        result = ''
        prev = self.countAndSay(n-1)
        temp_count = 1
        for i in range(len(prev)-1):
            if prev[i]==prev[i+1]:
                temp_count+=1
            else:
                result += str(temp_count) + prev[i]
                temp_count=1
            if i==len(prev)-2 and prev[i] != prev[i+1]:
                result += '1'+prev[-1]
            elif i==len(prev)-2 and prev[i] == prev[i+1]:
                result += str(temp_count) + prev[i]
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(7))