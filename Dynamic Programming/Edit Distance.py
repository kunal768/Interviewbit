# https://www.geeksforgeeks.org/edit-distance-dp-5/
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        n,m = len(A),len(B)
        if n ==0 or m == 0 :
            return m or n 
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                if i == 0 :
                    dp[i][j] = j
                elif j == 0 :
                    dp[i][j] = i
                
                elif A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])
        
        return dp[n][m]
    
