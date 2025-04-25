'''
Inspired by 
https://www.youtube.com/watch?v=4SP_AY7GGxw

Goal: find the difference between 2 given strings
'''

class Recursive_Solution:
    '''
    Pretty unefficient!
    '''
    def solve(self,s1, s2):
        def rec(s1, s2, i1, i2):
            if i1==len(s1) or i2==len(s2):
                return ''

            if s1[i1]==s2[i2]:
                return s1[i1] + rec(s1,s2,i1+1,i2+1)
            resultA = rec(s1, s2, i1, i2+1)
            resultB = rec(s1, s2, i1+1, i2)
            return resultA if len(resultA)>len(resultB) else resultB
        return rec(s1, s2, 0, 0)

class DP_LCS:
    def solve(self, s1, s2):
        def dp(s1, s2, i1, i2, memo):
            if i1==len(s1) or i2==len(s2):
                return ''

            if memo[i1][i2]:
                return memo[i1][i2]
            
            if s1[i1]==s2[i2]:
                memo[i1][i2] = s1[i1] + dp(s1,s2,i1+1,i2+1, memo)
                return memo[i1][i2]
            resultA = dp(s1, s2, i1, i2+1, memo)
            resultB = dp(s1, s2, i1+1, i2, memo)
            result  = resultA if len(resultA)>len(resultB) else resultB
            memo[i1][i2] = result
            return result

        memo = [[None for _ in range(len(s2))] for _ in range(len(s1)) ]
        return dp(s1, s2, 0, 0, memo)

if __name__ == "__main__":
    solution = DP_LCS()
    t = ('ABCD', 'AFKD')
    print(solution.solve(t[0], t[1]))
    t = ('I am waiting for the snow.', "I've been waiting for the snow.")
    print(solution.solve(t[0], t[1]))
