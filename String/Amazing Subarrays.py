class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        hs = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I' , 'O', 'U' }
        x = 0 
        for i in range(len(A)):
            if A[i] in hs :
                x += len(A)-i
        return x%10003
