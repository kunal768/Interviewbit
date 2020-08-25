class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        if not A :
            return []
        level = 0
        ans = []
        q = [A]
        while q:
            if level & 1 == 0 :
                ans.append([x.val for x in q])
            else:
                ans.append([x.val for x in q][::-1])
            q = [x for n in q for x in (n.left,n.right) if x]
            level += 1
        return ans
