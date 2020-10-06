# Linear Space Complexity : TLE 
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        vis = set()
        for idx, i in enumerate(A) :
            if any(abs(i-v[0]) == B and i != v[1] for v in vis ) :
                return 1
            vis.add((i, idx))
        
        return 0 



# Constant Space Complexity : AC
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        n = len(A)
        for i in range(n-1) :
            for j in range(n-1,i,-1):
                if A[j] - A[i] == B :
                    return 1
                elif A[j] - A[i] < B :
                    break
        return 0 
        
