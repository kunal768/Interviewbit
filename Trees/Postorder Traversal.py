# recursive 
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        def dfs(root):
            if not root :
                return
            nonlocal ans 
            if root.left :
                dfs(root.left)
            if root.right:
                dfs(root.right)
            ans.append(root.val)
        dfs(root)
        return ans

# iterative
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if noroot:
            return []
        stack , ans = [root],[]
        while stack :
            temp = stack.pop()
            ans.append(temp.val)
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
        return ans[::-1]
