# -- solution 1 : im a Python coder so you should  expect this was coming
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        return [i for i in str(int("".join(map(str,A)))+1)]

# -- solution 2 : The DSA way Hint : Use a DeQue 

from collections import deque
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        carry = 0 
        ans = deque()
        first = True
        for i in reversed(A):
            val = i + carry + (1 if first else 0)
            if first :
                first = False
            if val > 9 :
                carry = val // 10
                val = val%10 
            else :
                carry = 0
            
            ans.appendleft(val)
            
        # print(ans)
        if carry > 0:
            ans.appendleft(carry)
        # remove leading zeroes if any 
        while ans[0] == 0 :
            ans.popleft()
        
        return list(ans)
        

        
        
            
            
