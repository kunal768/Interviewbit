class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        dp = [0]*(A+1)
        dp[0] = 1
        for i in range(1,A+1):
            dp[i] = i*dp[i-1]
            
        ans = []
        for i in range(A+1):
            ans.append(dp[A]//(dp[A-i]*dp[i]))
        return ans
