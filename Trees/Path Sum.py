from functools import lru_cache
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        if not A :
            return 0
        ans = 0
        @lru_cache(None)
        def dfs(node,summ):
            if not node :
                return 
            nonlocal ans
            if summ+node.val == B and not node.left and not node.right :
                ans = 1
                return 
            dfs(node.left,summ+node.val)
            dfs(node.right,summ+node.val)
        
        dfs(A,0)
        return ans
