
class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, A):
        if not A :
            return 
        if not A.left and not A.right :
            return A
        def dfs(root):
            if not root :
                return 
            root.left,root.right = root.right,root.left
            dfs(root.left)
            dfs(root.right)
        dfs(A)
        return A
            
