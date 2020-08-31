class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, arr, B):
        l,h,ans = 0,len(arr)-1,-1
        while l <= h :
            mid = (l+h)//2
            if arr[mid] == B:
                return mid 
            elif arr[mid] < B :
                l = mid + 1
            else:
                h = mid - 1
        return l
