"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
"""

class Solution:
    def dfs(self, result, s, temp_set):
        print(len(temp_set), s)
        if len(temp_set)>4 and s:
            return
        if len(temp_set)==4 and not s:
            print('.'.join(temp_set))
            result.append('.'.join(temp_set))
        if len(s)>=3 and int(s[:3])<=255:
            temp_set.append(s[:3])
            self.dfs(result, s[3:], temp_set)
            temp_set.pop()
        if len(s)>=2 and int(s[:2])<=255:
            temp_set.append(s[:2])
            self.dfs(result, s[2:], temp_set)
            temp_set.pop()
        if len(s)>=1 and int(s[:1])<=255:
            temp_set.append(s[:1])
            self.dfs(result, s[1:], temp_set)
            temp_set.pop()

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self.dfs(result, s, [])
        return result

if __name__ == "__main__":
    s = Solution()
    t1= "25525511135"
    print(s.restoreIpAddresses(t1))
    t2 = "010010"
    print(s.restoreIpAddresses(t2)) # ["0.10.0.10","0.100.1.0"]