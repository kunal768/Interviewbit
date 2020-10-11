class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if not A :
            return 0 
        ans = 0 
        deduct = A[0]
        for i in range(1, len(A)):
            deduct = min(deduct, A[i])
            ans = max(ans, A[i] - deduct)
        return ans

