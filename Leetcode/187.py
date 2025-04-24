"""
187. Repeated DNA Sequences

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

ROLLING HASH
"""
from collections import defaultdict
PATTERN_LENGTH = 10

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        L =  len(s)
        if L <= PATTERN_LENGTH:
            return []
        
        ret = []
        count_dict = defaultdict(int)
        for i in range(L-PATTERN_LENGTH+1):
            hazh = hash(s[i:i+PATTERN_LENGTH])
            count_dict[hazh] += 1
            if count_dict[hazh] == 2:
                ret.append(s[i:i+PATTERN_LENGTH])
        return ret

if __name__ == "__main__":
    solution = Solution()
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    output = ["AAAAACCCCC", "CCCCCAAAAA"]
    print(solution.findRepeatedDnaSequences(s))
    s = "AAAAAAAAAAA"
    output = ["AAAAAAAAAA"]
    print(solution.findRepeatedDnaSequences(s))
