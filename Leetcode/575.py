class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # notice how to get the distinct value
        distinct_types = set(candies)
        print(len(distinct_types))
        if len(distinct_types)==len(candies)//2:
            return len(distinct_types)
        elif len(distinct_types)<len(candies)//2:
            return len(distinct_types)
        else:
            return len(candies)//2
        

if __name__ == '__main__':
    solution = Solution()
    t1 = [1,1,2,2,3,3]
    print(solution.distributeCandies(t1))
    t2 = [1,1,2,3]
    print(solution.distributeCandies(t2))