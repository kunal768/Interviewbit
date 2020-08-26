# BFS with some tweak
class Solution:
    # @param A : root node of tree
    # @return an integer
    def minDepth(self, A):
        q = [(A,0)]
        dis = {}
        while q :
            node,d = q.pop(0)
            # if node is a leaf node, only then store distance
            if not node.left and not node.right:
                dis[node] = d
            if node.left :
                q.append((node.left,d+1))
            if node.right:
                q.append((node.right,d+1))
        
        return min(dis.values())+1
