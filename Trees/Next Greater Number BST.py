# -- BFS approach (Naive)
# Less Efficient 
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def getSuccessor(self, A, B):
        ans = None
        q = [A]
        # bfs
        while q :
            size = len(q)
            while size :
                size -= 1
                node = q.pop(0)
                if node.val > B :
                    if not ans :
                        ans = node
                    else:
                        if ans.val > node.val :
                            ans = node
                if node.left :
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
        return ans

# Better approach using properties of BST (i.e smaller number towards left and greater towards right)
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def getSuccessor(self, A, B):
        ans = None
        while A :
            if A.val > B:
                ans = A
                A = A.left 
            else:
                A = A.right 
        return ans
    
# Stack Based Inorder Approach 
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def getSuccessor(self,root ,B):
        stack,ans = [],[]
        if not root :
            return None
        previous = False
        while stack or root :
            while root :
                stack.append(root)
                root = root.left
            root = stack.pop()
            if previous :
                return root
            if not previous and root.val == B :
                previous = True
            root = root.right
        return None
            
        


