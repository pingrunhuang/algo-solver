'''  
A string S of lowercase letters is given. We want to partition this string into as many parts as possible 
so that each letter appears in at most one part, and return a list of integers representing the size of these parts. 
'''

class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last={}
        for i, s in enumerate(S):
            last[s]=i
        print(last)

        result=[]
        start_index=0
        end_index=0
        for i, s in enumerate(S):
            # this is how to dynamically assign the end index for each sub part
            end_index=max(last[s], end_index)
            if end_index==i:
                result.append(end_index-start_index+1)
                start_index=i+1
        return result


if __name__=='__main__':
    solution=Solution()
    test_case1="ababcbacadefegdehijhklij"
    print(solution.partitionLabels(test_case1))