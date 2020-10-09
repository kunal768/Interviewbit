class Solution:
    # @param A : list of list of integers
    # @return an integer
    def calculateMinimumHP(self, dungeon):
        n, m = len(dungeon), len(dungeon[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if i == n-1 and j == m-1 :
                    dp[i][j] = min(0, dungeon[i][j])
                elif i == n-1:
                    dp[i][j] = min(0, dungeon[i][j] + dp[i][j+1])
                
                elif j == m-1:
                    dp[i][j] = min(0, dungeon[i][j] + dp[i+1][j])
                
                else :
                    dp[i][j] = min(0, dungeon[i][j] + max(dp[i][j+1], dp[i+1][j]))
        
        return abs(dp[0][0]) + 1
                
                
