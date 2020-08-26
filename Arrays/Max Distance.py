
# Shaandar Algorithm : Hint : do the rain water trapping problem, uses similar concept
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, arr):
        maxx = 0 
        n = len(arr)
        lmin,rmax = [0]*n,[0]*n
        
        lmin[0] = arr[0]
        for i in range(1,n):
            lmin[i] = min(lmin[i-1],arr[i])
            
        rmax[-1] = arr[-1]
        for j in range(n-2,-1,-1):
            rmax[j] = max(arr[j],rmax[j+1])
        
        i,j = 0,0
        while j < n and i < n :
            if lmin[i] <= rmax[j] :
                maxx = max(maxx,j-i)
                j = j + 1
            else:
                i = i + 1
            
        return maxx
        
        
