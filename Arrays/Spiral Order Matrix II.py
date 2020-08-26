class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        matrix = [[0 for _ in range(A)] for _ in range(A)]
        ans = 1
        l,r,t,d = 0,A-1,0,A-1
        while l<=r and t<=d :
            for i in range(l,r+1):
                matrix[t][i] = ans
                ans += 1
            t += 1
            
            for i in range(t,d+1):
                matrix[i][r] = ans
                ans += 1
            r -= 1
            
            for i in range(r,l-1,-1):
                matrix[d][i] = ans
                ans +=1
            d -= 1
            
            for i in range(d,t-1,-1):
                matrix[i][l] = ans
                ans += 1
            l += 1
        
        return matrix
            
            
            
