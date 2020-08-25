# Morris inorder traversal 

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def recoverTree(self, A):
        x = y = predecessor = None
        def dfs(node):
            nonlocal x,y,predecessor
            if not node :
                return 
            if node.left :
                dfs(node.left)
            
            if predecessor and node.val < predecessor.val :
                y = node
                if not x :
                    x = predecessor
                else:
                    return 
            
            predecessor = node
            if node.right :
                dfs(node.right)
            
        dfs(A)
        x.val,y.val = y.val,x.val
        return [x.val,y.val]    
                
