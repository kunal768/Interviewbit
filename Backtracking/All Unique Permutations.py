class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        def dfs(path,visited):
            nonlocal res
            if len(path) == len(A):
                res.append(path)
                return 
            for i in range(len(A)):
                if not i in visited:
                    if i>0 and i-1 not in visited and A[i]==A[i-1] :
                        continue
                    visited.add(i)
                    dfs(path+[A[i]],visited)
                    visited.remove(i)
        A.sort()
        vis = set()
        res = []
        dfs([],vis)
        return res
