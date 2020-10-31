class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        if not A :
            return 0 
        # imagine doing 1d array problem 
        # now choose max for each column
        m = len(A[0])
        for i in range(m):
            A[0][i] = max(A[0][i], A[1][i])
        if m == 1 :
            return A[0][0]
        # same algo as 1-D problem
        A[0][1] = max(A[0][0], A[0][1])
        for i in range(2, m):
            A[0][i] = max(A[0][i-1], A[0][i-2]+A[0][i])
        
        return max(A[0][m-1], A[0][m-2])
