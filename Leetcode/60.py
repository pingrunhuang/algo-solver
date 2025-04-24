"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.

TODO: How to solve time limit exceed????
permutation and Combination
"""

class Solution:
    def genPermutation(self, result, n, temp_result):
        '''
        time limit exceeded!!!!
        '''
        if len(temp_result)==n:
            result.append(temp_result.copy())
        else:
            for num in range(1, n+1):
                if num in temp_result:continue
                temp_result.append(num)
                self.genPermutation(result, n, temp_result)
                temp_result.pop()
        return result

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ordered_permutations = []
        self.genPermutation(ordered_permutations, n, [])
        result = ''.join([str(x) for x in ordered_permutations[k-1]])
        print(result)
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.getPermutation(3, 3) == "213"
    assert s.getPermutation(4, 9) == "2314"
    assert s.getPermutation(9,24) == "123459876"