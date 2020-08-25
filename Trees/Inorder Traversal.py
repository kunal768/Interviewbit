# Recursion

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def inorderTraversal(self, A):
	    if not A :
	        return []
	    ans = []
	    def dfs(node):
	        if not node:
	            return
	        nonlocal ans
	        if node.left :
	            dfs(node.left)
	        ans.append(node.val)
	        if node.right:
	            dfs(node.right)
	    dfs(A)
	    return ans
	    
      
# Iterative O(n) space = O(n) using stack https://www.youtube.com/watch?v=QxFOR8sQuB4&feature=youtu.be
class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def inorderTraversal(self, root):
	    if not root :
	        return []
	    ans,stack = [],[]
	    while stack or root :
	        while root :
	            stack.append(root)
	            root = root.left
	        temp = stack.pop()
	        ans.append(temp.val)
	        if temp.right :
	            root = temp.right 
	    return ans


# Iterative O(1) space (Morris Jadugar)



