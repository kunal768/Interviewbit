class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        n = len(A)
        profit = 0 
        for i in range(1,n):
            profit += max(A[i]-A[i-1],0)
        return profit
