# Run on Python2 because Python3 compiler is fucked up 
class Solution:
    # @param A : string
    # @return an integer
    def longestValidParentheses(self, A):
        n = len(A)
        l,r,maxlen = 0,0,0
        for i in range(n):
            if A[i] == '(':
                l += 1
            else:
                r += 1
            
            if l == r :
                maxlen = max(maxlen,2*r)
            elif r > l :
                l = 0
                r = 0 
        
        l = r = 0 
        for i in range(n-1,-1,-1):
            if A[i] == '(':
                l += 1
            else:
                r += 1
            if l == r :
                maxlen = max(maxlen,2*l)
            
            elif l > r :
                l = 0
                r = 0 
        
        return maxlen
            
