"""345. Reverse Vowels of a String
"""

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        head = 0
        tail = len(s)-1
        result = list(s)
        while head<tail:
            if s[tail] not in vowels:
                result[tail] = s[tail]
                tail-=1
            if s[head] not in vowels:
                result[head] = s[head]
                head+=1
            if s[head] in vowels and s[tail] in vowels:
                result[head] = s[tail]
                result[tail] = s[head]
                head+=1
                tail-=1
        result_s = ""
        for i in result:
            result_s+=i
        return result_s

if __name__ == "__main__":
    solution = Solution()
    t1 = "hello"
    print(solution.reverseVowels(t1))
    t2 = "leetcode"
    print(solution.reverseVowels(t2))