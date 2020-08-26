# Straight Forward BFS question
class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxDepth(self, A):
        q = [(A,0)]
        dis = {}
        while q :
            node,d = q.pop(0)
            dis[node] = d
            if node.left :
                q.append((node.left,d+1))
            if node.right:
                q.append((node.right,d+1))
        
        return max(dis.values())+1
