class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        symbols, brackets = 0, 0 
        hs = {"+", "-", "*", "/"}
        
        for i in range(len(A)):
            if i + 2 < len(A) and A[i] == '(' and A[i+2] == ')':
                return 1
            if A[i] in hs :
                symbols += 1
            
            elif A[i] == '(':
                brackets += 1
            
        if brackets > symbols :
            return 1
        
        return 0
