class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        if A == 0 :
            return []
        if A == 1 :
            return [[1]]
        dp = [0]*(A+1)
        dp[0] = 1
        for i in range(1,A+1):
            dp[i] = i*dp[i-1]
        new = [[1]]
        for i in range(1,A):
            ans = []
            for j in range(i+1):
                ans.append(dp[i]//(dp[i-j]*dp[j]))
            new.append(ans)
        return new
            
        
