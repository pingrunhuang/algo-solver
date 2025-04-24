class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        s_list = s.split()
        return " ".join(s_list[::-1])
    

if __name__ == "__main__":
    s = Solution()
    t = "the sky is blue"
    assert s.reverseWords(t) == "blue is sky the"
    t = "a good   example"
    assert s.reverseWords(t) == "example good a"
    t = "  hello world!  "
    assert s.reverseWords(t) == "world! hello"
