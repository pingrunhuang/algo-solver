"""
TODO
"""

class Solution_naive(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        hashWorldDict = dict.fromkeys(wordDict, True)
        i = 0
        j = 0
        s_length = len(s)
        while i < s_length:
            i+=1
            cur_word = s[j:i]
            if hashWorldDict.get(cur_word):
                j = i
        if i!=j:
            return False
        else:
            return True

class Solution(object):
    def dfs(self, s, word_set, index):
        """
        index keep track of the current pointer to the string
        """
        # base case 
        if index == len(s):
            return True

        if index in self.no_match_word_index_set:
            return False
        for i in range(index+1, len(s)+1):
            sub_str = s[index:i]
            if sub_str in word_set:
                if self.dfs(s, word_set, i):
                    return True
                else:
                    self.no_match_word_index_set.add(i)

        self.no_match_word_index_set.add(index)
        return False
    
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # keep track of if there exists a set of words in the wordDict that could assemble to s[:index]
        self.no_match_word_index_set = set()
        return self.dfs(s, set(wordDict), 0)



if __name__ == "__main__":
    s = Solution()
    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    assert s.wordBreak(s1, wordDict1) == True

    s2 = "applepenapple" 
    wordDict2 = ["apple", "pen"]
    assert s.wordBreak(s2, wordDict2) == True

    s3 = "catsandog" 
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    assert s.wordBreak(s3, wordDict3) == False

    s4 = "aaaaaaa"
    wordDict4 = ["aaaa","aaa"]
    assert s.wordBreak(s4, wordDict4) == True

    # time limit case 
    s5 = "bccdbacdbdacddabbaaaadababadad"
    wordDict5 = ["cbc","bcda","adb","ddca","bad","bbb","dad","dac","ba","aa","bd","abab","bb","dbda","cb","caccc","d","dd","aadb","cc","b","bcc","bcd","cd","cbca","bbd","ddd","dabb","ab","acd","a","bbcc","cdcbd","cada","dbca","ac","abacd","cba","cdb","dbac","aada","cdcda","cdc","dbc","dbcb","bdb","ddbdd","cadaa","ddbc","babb"]
    s.wordBreak(s5, wordDict5)