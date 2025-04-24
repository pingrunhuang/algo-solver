

class Solution:
    def findCommon(self, s1, s2):
        n1 = len(s1)
        n2 = len(s2)
        if n1==0 or n2==0:
            return False
        p1 = 0
        p2 = 0
        while p1<n1 and p2<n2:
            if s1[p1]==s2[p2]:
                p1+=1
                p2+=1
            else:
                p1+=1
        if p2==n2:
            return True
        else:
            return False

    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d = sorted(d, key=lambda x: (-len(x), x))
        for word in d:
            if self.findCommon(s, word):
                return word
        return ""


if __name__ == "__main__":
    solution = Solution()
    s1, d1 = "abpcplea", ["ale","apple","monkey","plea"]
    print(solution.findLongestWord(s1, d1))
    s2, d2 = "abpcplea", ["a","b","c"]
    print(solution.findLongestWord(s2, d2))
    s3, d3 = "bab", ["ba","ab","a","b"]
    print(solution.findLongestWord(s3,d3))