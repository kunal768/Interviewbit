class Solution:
    # @param A : string
    # @return an integer
    def anytwo(self, A):
        def lcs(a,b):
            n,m = len(a),len(b)
            if n == 0 or m == 0 :
                return 0 
            dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
            for i in range(1,n+1):
                for j in range(1,m+1):
                    if a[i-1] == b[j-1] and i != j :
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            return (1 if dp[n][m] >= 2 else 0)
        
        
        return lcs(A,A)
            
