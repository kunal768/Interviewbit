class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        vis = set()
        for i in A :
            if ((i - B) in vis) or (i + B in vis):
                return 1
            vis.add(i)
        return 0 
                
