class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        def first(arr,x):
            l,h = 0,len(arr)-1
            ans = -1
            while l<= h :
                mid = (l+h)//2
                if arr[mid] == x :
                    ans = mid
                    h = mid - 1
                elif arr[mid] > x :
                    h = mid - 1
                else:
                    l = mid +1
            return ans
        
        def last(arr,x):
            l,h,ans = 0,len(arr)-1,-1
            while l <= h :
                mid = (l+h)//2
                if arr[mid] == x :
                    ans = mid 
                    l = mid + 1
                elif arr[mid] > x :
                    h = mid - 1
                else:
                    l = mid + 1
            
            return ans
        x,y = first(A,B),last(A,B)
        return [x,y]
        
        
        
        
        
