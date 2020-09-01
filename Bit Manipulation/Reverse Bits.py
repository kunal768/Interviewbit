class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        x = 0
        for i in range(32):
            if A&1<<i :
                x = x|1 << 31-i
        return x
