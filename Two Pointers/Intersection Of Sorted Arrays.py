class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        i, j = 0, 0 
        ans = []
        # let B always be the bigger array (not needed tho)
        if len(A) > len(B) :
            A, B = B, A
        
        while i < len(A) and j < len(B):
            while i < len(A) and j < len(B) and A[i] == B[j] :
                ans.append(A[i])
                i += 1
                j += 1
            
            while i < len(A) and j < len(B) and A[i] < B[j] :
                i += 1
            
            while i < len(A) and j < len(B) and A[i] > B[j] :
                j += 1
            
        return ans
                
