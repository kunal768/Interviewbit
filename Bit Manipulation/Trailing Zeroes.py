class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, n):
        for i in range(32):
            if n & 1 << i :
                return i 
        return 0
