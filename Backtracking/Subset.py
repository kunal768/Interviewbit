class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        res = []
        n = len(A)
        A.sort()
        def dfs(curr = [],index = 0):
            nonlocal res,n
            if len(curr) == k :
                res.append(curr[:])
                # return 
            for i in range(index,n):
                curr.append(A[i])
                dfs(curr,i+1)
                curr.pop()
        
        for k in range(n+1):
            dfs()
        return sorted(res)
