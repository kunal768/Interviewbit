class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, A):
        i = len(A)-2
        while i >= 0 and A[i+1] <= A[i]:
            i -= 1
        
        if i >= 0 :
            j = len(A)-1
            while j >= 0 and A[j] <= A[i] :
                j -= 1
            A[i],A[j] = A[j],A[i]
        A[i+1:] = A[i+1:][::-1]
    
        return A
            
            
            
            
            
            
            
