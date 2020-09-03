class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return a list of integers
    def solve(self, A, B, C, D):
        dp = [1]
        i,j,k = 0,0,0
        while len(dp) <= D :
            m = min(dp[i]*A,dp[j]*B,dp[k]*C)
            dp.append(m)
            if A*dp[i] == m:
                i += 1
            if B*dp[j] == m :
                j += 1
            if C*dp[k] == m :
                k += 1
        
        return dp[1:]        
            
                
