

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        movement={
            'U':(0,1),
            'D':(0,-1),
            'R':(1,0),
            'L':(-1,0)
        }
        result = (0,0)
        for e in moves:
            result = (result[0]+movement[e][0], result[1]+movement[e][1])
        if result==(0,0):
            return True
        else:
            return False

if __name__=='__main__':
    solution = Solution()
    print(solution.judgeCircle("UD"))