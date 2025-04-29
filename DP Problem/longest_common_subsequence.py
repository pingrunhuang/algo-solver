"""
A very common problem in computer science is to find the longest common subsequence (LCS) of two subsequences.

The LCS is the longest sequence that can be derived from both sequences by deleting some characters without changing the order of the remaining characters.
For example, the LCS of "ABCD" and "AFKD" is "AD", and the LCS of "I am waiting for the snow." and "I've been waiting for the snow." is "I am waiting for the snow.".




Transition formular:
LCS(n,m) represent LCS between 2 strings with length of n and length of m. Let's check the prefix of these 2 strings A and B.
if A[n-1]!=B[m-1]: LCS(n,m) = max(LCS(n-1,m), LCS(n,m-1))
if A[n-1]==B[m-1]: LCS(n,m) = LCS(n-1,m-1)+1
base case: LCS(n,0) = LCS(0,m)=0


usage of LCS: git diff
An O(ND) difference algorithm and variations
"""


def longest_common_subsequence(a:list,b:list)->int:
    n = len(a)
    m = len(b)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1, m+1):
            if a[i-1]!=b[j-1]:
                dp[i][j] = max([dp[i-1][j], dp[i][j-1]])
            else:
                dp[i][j] = dp[i-1][j-1] + 1
    for x in dp:
        print(x)
    lcs = reconstruct_elements(dp, a, b)
    print("LCS: ", lcs)
    return dp[-1][-1]

def reconstruct_elements(dp:list[list], a:list, b:list)->list:
    i = len(a)
    j = len(b)
    result = []
    while i>0 and j>0:
        if a[i-1]==b[j-1]:
            result.append(a[i-1])
            i-=1
            j-=1
        elif dp[i-1][j]==dp[i][j-1]:
            i-=1
        else:
            j-=1
    result.reverse()
    return result
if __name__ == "__main__":
    print(longest_common_subsequence([6,4,5,9,11],[1,4,5,6,9,10,11]))
    # print(longest_common_subsequence([],[1,15,4,5,6,9,11]))
    # print(longest_common_subsequence([],[]))
    # print(longest_common_subsequence([1,2,3,4,5],[1,2,3,4,5]))
