class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        A.sort()
        res = []
        def dfs(path,vis):
            nonlocal res
            if len(path) == len(A):
                res.append(path)
                return 
            
            for i in range(len(A)):
                if not A[i] in vis :
                    vis.add(A[i])
                    dfs(path+[A[i]],vis)
                    vis.remove(A[i])
        vis = set()
        dfs([],vis)
        return res
