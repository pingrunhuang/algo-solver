'''
DP DFS 
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

The idea is to change complexity from O(n^n) to O(2*n)
'''

class Solution:
    def dfs(self, digits, result, cur_str):
        if digits=='':
            result.append(cur_str)
            return
        for letter in self.digits_letters_mapping[digits[0]]:
            self.dfs(digits[1:], result, cur_str+letter)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=='':
            return []
        self.digits_letters_mapping = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        result = []
        self.dfs(digits, result, '')
        return result

from functools import reduce
class Solution2:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if '' == digits: return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])
        
class DP:
    def letterCombinations(self, digits):
        digits_letters_mapping={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        dp = []
        for digit in digits:
            if not dp:
                # convert the string into a list of char
                dp = list(map(lambda x:x, digits_letters_mapping[digit]))
            else:
                temp = list(map(lambda x: (x + y  for y in digits_letters_mapping[digit]), dp))
                dp = []
                for t in temp:
                    dp.extend(t)
        return dp

    def letterCombinations2(self, digits):
        digits_letters_mapping={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        dp = []
        for digit in digits:
            if not dp:
                dp = list(digits_letters_mapping[digit])
            else:
                temp, dp = [x+y for x in dp for y in digits_letters_mapping[digit]], []
                dp += temp
        return dp



if __name__ == "__main__":
    s = DP()
    t1 = '234'
    e1 = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    print(s.letterCombinations2(t1))
