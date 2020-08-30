class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, target):
        n,m = len(A),len(A[0])
        col = m-1
        for i in range(n):
            while col >= 0 and A[i][col] > target:
                col -= 1
            
            if col >= 0 and A[i][col] == target :
                return 1
        
        return 0
