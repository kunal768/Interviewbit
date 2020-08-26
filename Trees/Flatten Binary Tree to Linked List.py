class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, root):
        if not root:
            return root
        stack = [root]
        while stack :
            node = stack.pop()
            if node.right :
                stack.append(node.right)
            
            if node.left:
                stack.append(node.left)
                
            if stack :
                node.right = stack[-1]
                
            node.left = None
        
        return root
            
