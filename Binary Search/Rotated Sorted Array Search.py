class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, arr, x):
        l,h,ans = 0,len(arr)-1,-1
        n = len(arr)
        minn = None
        while l <= h :
            mid = (l+h)//2
            prev = (mid+n-1)%n
            nextt = (mid+1)%n
            if arr[mid] <= arr[prev] and arr[mid] <= arr[nextt]:
                minn = mid 
                break 
            elif arr[mid] < arr[h]:
                h = mid - 1
            elif arr[l] <= arr[mid] :
                l = mid + 1
        
        def  bsearch(l,h,x):
            ans = -1
            while l <= h :
                mid = (l+h)//2
                if arr[mid] == x :
                    return mid
                elif arr[mid] > x :
                    h= mid - 1
                else:
                    l = mid + 1
            
            return ans 
            
        l,r = bsearch(0,minn-1,x),bsearch(minn,n-1,x)
        if l == -1 :
            return r
        elif r == -1 :
            return l
        return -1
        
        
                
            
