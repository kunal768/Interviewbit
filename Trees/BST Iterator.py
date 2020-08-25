# O(n) space approach n :  number of nodes
def inorder(root,ans):
    if not root :
        return 
    if root.left :
        inorder(root.left,ans)
    ans.append(root.val)
    if root.right:
        inorder(root.right,ans)


class BSTIterator:
    # @param root, a binary search tree's root node

    def __init__(self, root):
        self.arr = []
        inorder(root,self.arr)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self): 
        return len(self.arr) > 0

    # @return an integer, the next smallest number
    def next(self):
        if self.arr :
            return self.arr.pop(0)
        else:
            pass 


# O(h) space approach h : height of BST https://leetcode.com/problems/binary-search-tree-iterator/solution/







class BSTIterator:

    def __init__(self, root: TreeNode):
        
        # Stack for the recursion simulation
        self.stack = []
        
        # Remember that the algorithm starts with a call to the helper function
        # with the root node as the input
        self._leftmost_inorder(root)
        
    def _leftmost_inorder(self, root):
        
        # For a given node, add all the elements in the leftmost branch of the tree
        # under it to the stack.
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        
        # Node at the top of the stack is the next smallest element
        topmost_node = self.stack.pop()
        
        # Need to maintain the invariant. If the node has a right child, call the 
        # helper function for the right child
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0





