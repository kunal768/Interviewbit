class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        n,m = len(A),len(A[0])
        l,r,t,d = 0,m-1,0,n-1
        ans = []
        direction = 0 
        while l<= r and t <= d :
            if direction == 0 :
                for i in range(l,r+1):
                    ans.append(A[t][i])
                t += 1
            elif direction == 1 :    
                for i in range(t,d+1):
                    ans.append(A[i][r])
                r -= 1
            elif direction == 2 :
                for i in range(r,l-1,-1):
                    ans.append(A[d][i])
                d -= 1
            elif direction == 3 :
                for i in range(d,t-1,-1):
                    ans.append(A[i][l])
                l += 1
            direction = (direction+1)%4
        return ans
            
            
