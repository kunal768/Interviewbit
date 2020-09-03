class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        ans = -1
        i = 0 
        if not n :
            return ans
        A.sort()
        while i < n :
            while i+1 < n and A[i] == A[i+1]:
                i += 1
            
            if n-(i+1) == A[i]:
                ans = 1
                break
            i += 1
        return ans
