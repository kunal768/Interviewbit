class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        l,h,ans = 0,A,-1
        def isSafe(mid):
            return mid*mid >= A
            
        while l <= h :
            mid = (l+h)//2
            if isSafe(mid):
                ans = mid 
                h = mid - 1
            else:
                l = mid + 1
        
        return ans if ans*ans == A else ans - 1
