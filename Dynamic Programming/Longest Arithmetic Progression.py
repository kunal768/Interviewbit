from collections import defaultdict
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        if n <= 1 :
            return n 
        ans = 0
        dp = defaultdict(lambda : 1)
        for i in range(1, n):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i, diff] = dp[j, diff] + 1
                ans = max(ans, dp[i, diff])
        return ans
