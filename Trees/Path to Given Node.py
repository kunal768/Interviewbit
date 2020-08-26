class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        ans = []
        def dfs(res,path):
            nonlocal ans
            if not res :
                return 
            if res.val == B :
                if path :
                    path.append(res.val)
                    ans = path
                return
            dfs(res.left,path+[res.val])
            dfs(res.right,path+[res.val])
        
        dfs(A,[])
        return ans
        
