"""
mirror to leecode 95
"""
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        define F(i,n) as i as root and n numbers of node to be included
        Given i as root, get the number unique tree
        numTrees(n) = sum([F(i,n) for i in range(n)])

        numTrees(n) = sum(numTrees(i-1)*numTrees(n-i) for i in range(n))
        """
        g = [0]*(n+1)
        g[0], g[1] = 1,1
        
        for root in range(2,n+1):
            for i in range(1,root+1):
                g[root] += g[i-1]*g[root-i]
        return g[n]

if __name__ == "__main__":
    s = Solution()
    print(s.numTrees(7))