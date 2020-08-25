# -- With Extra Space
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def kthsmallest(self, root, k):
        if not root :
            return -1
        ans = []
        def inorder(root,ans):
            if not root :
                return 
            inorder(root.left,ans)
            ans.append(root.val)
            inorder(root.right,ans)
        inorder(root,ans)
        return ans[k-1]
  
  # Without Extra Space Using BST properties 
