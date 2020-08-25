# recursive
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def dfs(node):
            nonlocal ans
            if not node:
                return 
            ans.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)   
        return ans

# iterative
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack,ans = [root],[]
        while stack:
            temp = stack.pop()
            ans.append(temp.val)
            if temp.right :
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
        return ans
