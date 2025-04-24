

class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result=[]
        for i in range(left,right+1):
            if self.isSelfDividing(i):
                result.append(i)
        return result
    
    def isSelfDividing(self, num):
        temp_num=num
        while temp_num>0:
            division = temp_num%10
            # int(2/10)=0 equivalent to floor
            temp_num=int(temp_num/10)
            if division==0:
                return False
            if num%division!=0:
                return False
        return True


if __name__=='__main__':
    solution = Solution()
    print(solution.selfDividingNumbers(1,22))