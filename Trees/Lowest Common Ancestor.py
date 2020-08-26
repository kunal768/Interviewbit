class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, root, n1, n2):
        def find(root,val):
            if not root :
                return False
            if root.val == val :
                return True
            
            if (root.left and find(root.left,val)) or (root.right and find(root.right,val)) :
                return True
            return False
        
        def LCA(root,n1,n2):
            if not root or root.val == n1 or root.val == n2:
                return root  
            l,r = LCA(root.left,n1,n2),LCA(root.right,n1,n2)
            if l and r :
                return root
            return l if l else r 
            
        if not find(root,n1) or not find(root,n2):
            return -1
        ans = LCA(root,n1,n2)
        if ans :
            return ans.val
        return -1
        
   
