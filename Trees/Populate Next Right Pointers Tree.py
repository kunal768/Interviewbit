class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        q = [root]
        while q :
            for i in range(len(q)-1):
                q[i].next = q[i+1]
            q[-1].next = None
            q = [x for n in q for x in (n.left,n.right) if x]
                
