class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        x = 0 
        for i in A :
            x ^= i 
        return x
