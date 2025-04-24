"""
lcp: longest common prefix

This question is equivilant to leetcode 2573.Find the string with lcp

There was a string of length n made up of lowercase english letters. The string was used to create a 2-dimensional array,
lcp[n][n], such that lcp[i][j] is equal to the length of the longest common prefix between the substrings s[i:n] and s[j:n]
for every 1 <=i,j<=n. it is possible that lcp has been corrupted. Given lcp[n][n], return the alphabetically smallest string of length
n that conforms to lcp. If there is no such string, return the string Impossible.
"""

def getStringByLCP(lcp):
    n = len(lcp)
    word = [None] * n

    for i in range(n):
        # Find the lexicographically smallest character that satisfies the current lcp condition
        for ch in range(ord('a'), ord('z') + 1):
            char = chr(ch)
            valid = True

            for j in range(n):
                if word[j] is not None and lcp[i][j] != n - i:
                    valid = False
                    break
                if word[j] is None and lcp[i][j] != min(lcp[i][i], n - j):
                    valid = False
                    break

            if valid:
                word[i] = char
                break

    return ''.join(word) if None not in word else ""

if __name__=="__main__":
    lcp = [
        [3,0,0],
        [0,2,1],
        [0,1,1]
    ]
    print(getStringByLCP(lcp))