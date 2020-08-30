class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        o,c = 0,0
        for i in range(len(A)-2):
            if A[i] =='(' and A[i+2] == ')' :
                return 1
            if A[i] in {'*','+','-','/'}:
                o += 1
            elif A[i] == '(':
                c += 1
        if c > o :
            return 1
        return 0
