'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.
'''

class Solution:
    def addBit(self, num1, num2, add_one):
        '''
        :return: 
        add_one
        cur_num
        '''
        if add_one=='0':
            if num1=='1' and num2=='1':
                return '1', '0'
            if (num1=='1' and num2=='0') or (num1=='0' and num2=='1'):
                return '0', '1'
            else:
                return '0', '0'
        else:
            if num1=='1' and num2=='1':
                return '1', '1'
            if (num1=='1' and num2=='0') or (num1=='0' and num2=='1'):
                return '1', '0'
            else:
                return '0', '1'            

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result_queue = []
        a_stack = list(a)
        b_stack = list(b)
        add_one = '0'
        while a_stack or b_stack:
            num_a='0'
            num_b='0'
            if a_stack:
                num_a = a_stack.pop()
            if b_stack:
                num_b = b_stack.pop()
            add_one, cur_num = self.addBit(num_a, num_b, add_one)
            result_queue.insert(0,str(cur_num))
        if add_one=='1':
            result_queue.insert(0, add_one)
        return ''.join(result_queue)

class Solution2:
    '''
    Slowest!
    '''
    def addBinary(self, a, b):
        result = []
        i = len(a)-1
        j = len(b)-1
        add_one = 0
        temp_result = 0

        while i>=0 or j>=0:
            temp_result = add_one
            if i>=0:
                temp_result += int(a[i])
                i-=1
            if j>=0:
                temp_result += int(b[j])
                j-=1
            result.insert(0, str(temp_result%2))
            add_one=temp_result//2
        if add_one!=0:
            result.insert(0, str(add_one))
        return ''.join(result)

class Solution3:
    '''
    Python solution
    '''
    def addBinary(self, a, b):
        return bin(eval('0b'+a)+eval('0b'+b))[2:]

class Solution4:
    '''
    Recursive
    '''
    def addBinary(self, a, b):
        # base case
        if len(a)==0:
            return b
        if len(b)==0:
            return a
        
        if a[-1]=='1' and b[-1]=='1':
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
        if a[-1]=='0' and b[-1]=='0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'

if __name__ == "__main__":
    s = Solution4()
    a = "11"
    b = "1"
    assert s.addBinary(a,b)=='100'
    a = '1010'
    b = '1011'
    assert s.addBinary(a, b)=='10101'
            