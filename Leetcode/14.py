"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


"""
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ''
        shortest_len = min(len(x) for x in strs)
        common_prefix = ""
        for col in range(shortest_len):
            prev_char = strs[0][col]
            for row in range(len(strs)):
                if strs[row][col]!=prev_char:
                    return common_prefix
            common_prefix+=strs[0][col]
        return common_prefix

if __name__ == "__main__":
    s = Solution()
    t1 = ["flower","flow","flight"]
    print(s.longestCommonPrefix(t1))
    t2 = ["dog","racecar","car"]
    print(s.longestCommonPrefix(t2))