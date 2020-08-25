# Recursive (TLE) Dont stress about it they've just fucked up everything for Python and Java
class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, root):
        if not root :
            return 1
        def same(a,b):
            if not a and not b :
                return True 
            elif not a or not b :
                return False
            return a.val == b.val and same(a.left,b.right) and same(a.right,b.left)
        
        return int(same(root,root))
        

# Iterative
class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, root):
        if not root or (not root.left and not root.right):
            return 1
        q = [root,root]
        while q :
            l , r = q.pop(0),q.pop(0)
            if l.val != r.val :
                return 0
            if l.left and r.right:
                q.append(l.left)
                q.append(r.right)
            elif l.left or r.right:
                return 0
            
            if l.right and r.left:
                q.append(l.right)
                q.append(r.left)
            elif l.right or r.left:
                return 0 
        return 1
