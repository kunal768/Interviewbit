class Solution:
    # @param A : list of strings
    # @return an integer
    def black(self, arr):
        n = len(arr)
        m = 0
        if n == 0 :
            return 0 
        if n > 0 :
            m = len(arr[0])
        A = []
        for row in arr :
            A.append([i for i in row])
        # print(A)
        vis = [[0 for _ in range(m+1)] for _ in range(n+1)]
            
        def issafe(x,y):
            return x >= 0 and x<n and y >= 0 and y < m and not vis[x][y] and A[x][y] == 'X'
            
        def dfs(x,y):
            if not issafe(x,y):
                return 
            vis[x][y] = 1
            A[x][y] = 'O'
            dfs(x+1,y)
            dfs(x,y+1)
            dfs(x,y-1)
            dfs(x-1,y)
        
        c = 0
        for i in range(n):
            for j in range(m):
                if A[i][j] == 'X' and not vis[i][j] :
                    dfs(i,j)
                    c += 1
        return c
        
        
        
        
            

