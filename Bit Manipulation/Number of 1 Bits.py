class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        c = 0 
        while A :
            c += 1
            A = A & (A-1)
        return c
