class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        for i in range(len(A)):
            for j in range(i+1,len(A[0])):
                A[i][j],A[j][i] = A[j][i],A[i][j]
        for i in range(len(A)):
            A[i] = A[i][::-1]
        return A
