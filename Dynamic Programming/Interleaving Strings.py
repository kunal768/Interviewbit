class Solution:
    # @param A : string
    # @param B : string
    # @param C : string
    # @return an integer
    def isInterleave(self, A, B, C):
        m,n = len(A),len(B)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        
        if m + n != len(C):
            return 0
        
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j ==0 :
                    dp[i][j] = True
                elif i == 0 :
                    if B[j-1] == C[j-1] :
                        dp[i][j] = dp[i][j-1]
                elif j == 0 :
                    if A[i-1] == C[i-1] :
                        dp[i][j] = dp[i-1][j] 
                    
                elif A[i-1] == C[i+j-1] and B[j-1] != C[i+j-1]:
                    dp[i][j] = dp[i-1][j]
                elif A[i-1] != C[i+j-1] and B[j-1] == C[i+j-1] :
                    dp[i][j] = dp[i][j-1]
                elif A[i-1] == C[i+j-1] and B[j-1] ==C[i+j-1] :
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                
        return int(dp[m][n])
                
                
                    
