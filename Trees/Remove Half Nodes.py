class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def solve(self, A):
        def remove(root):
            if not root :
                return root
            
            root.left = remove(root.left)
            root.right = remove(root.right)
            
            if not root.left and not root.right:
                return root
            
            if not root.left:
                new = root.right
                temp = root
                root = None
                del(temp)
                return new
            
            if not root.right:
                new = root.left
                temp = root
                root = None
                del(temp)
                return new
            
            return root
        
        return remove(A)
            
        
