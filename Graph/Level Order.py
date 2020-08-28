# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        ans = []
        if not A :
            return ans
        q = [A]
        while q :
            ans.append([x.val for x in q])
            q = [x for n in q for x in (n.left,n.right) if x]
        return ans
