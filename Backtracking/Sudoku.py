class Solution:
    # @param A : list of list of chars
    # @return nothing
    def solveSudoku(self, A):
        def used_in_row(row,num):
            for i in range(9):
                if A[row][i] == num :
                    return True
            return False
        
        def used_in_col(col,num):
            for i in range(9):
                if A[i][col] == num:
                    return True
            return False
        
        def used_in_box(row,col,num):
            for i in range(3):
                for j in range(3):
                    if A[row+i][col+j] == num :
                        return True
            return False
        
        def issafe(row,col,num):
            return not used_in_row(row,num) and not used_in_col(col,num) and not used_in_box(row-row%3,col-col%3,num)
        
        
        def solve(arr):
            start = [-1,-1]
            for i in range(9):
                for j in range(9):
                    if arr[i][j] == '.':
                        start[0] = i
                        start[1] = j
                        break
            if start[0] == -1 and start[1] == -1 :
                return True
            
            for i in range(1,10):
                if issafe(start[0],start[1],str(i)):
                    arr[start[0]][start[1]] = str(i)
                    if solve(arr):
                        return True 
                    arr[start[0]][start[1]] = '.'
                    
            return False
            
        solve(A)
        
        
        
        
