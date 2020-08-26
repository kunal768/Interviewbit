class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        curr,maxx = float('-inf'),float('-inf')
        for i in A :
            curr = max(i,curr+i)
            maxx = max(maxx,curr)
        return maxx
