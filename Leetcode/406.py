
'''
hint:
the lowest is irrelevent to th others
'''

class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # sort the list by from heighest to lowest
        # if with the same height, the one with the smaller index should be inserted first
        people.sort(key=lambda x:(-x[0],x[1]))
        result=[]
        for p in people:
            result.insert(p[1],p)
    
        return result
        

        

if __name__=='__main__':
    t1=[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    solution = Solution()
    print("expected:",[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]])
    print(solution.reconstructQueue(t1))
    t2=[[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]
    print("expected:",[[3,0],[6,0],[7,0],[5,2],[3,4],[5,3],[6,2],[2,7],[9,0],[1,9]])
    print(solution.reconstructQueue(t2))