class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        l,h,mid = 0,len(A)-1,0
        while mid<=h :
            if A[mid] == 0:
                A[l],A[mid] = A[mid],A[l]
                l += 1
                mid += 1
            elif A[mid] == 1:
                mid += 1
            else:
                A[mid],A[h] = A[h],A[mid]
                h -= 1
        
        return A
