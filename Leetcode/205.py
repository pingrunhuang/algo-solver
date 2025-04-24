class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_map = {}
        i = 0
        min_len = min(len(s), len(t))
        while i < min_len:
            if char_map.get(s[i]):
                if char_map.get(s[i]) == t[i]:
                    i+=1
                else:
                    return False
            else:
                if t[i] in char_map.values():
                    # multi mapping
                    return False
                else: 
                    char_map[s[i]] = t[i]
                    i+=1
        return True


if __name__ == "__main__":
    s = Solution()
    t = ('egg', 'add')
    assert s.isIsomorphic(t[0], t[1]) is True
    t = ('foo', 'bar')
    assert s.isIsomorphic(t[0], t[1]) is False
    t = ('paper', 'title')
    assert s.isIsomorphic(t[0], t[1]) is True
    t = ("ab", "aa")
    assert s.isIsomorphic(t[0], t[1]) is False
    t = ('bar', 'foo')
    assert s.isIsomorphic(t[0], t[1]) is False
    

