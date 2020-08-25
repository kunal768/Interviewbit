
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, root, B):
        q = [root]
        ans = []
        found = False
        while q and not found:
            size = len(q)
            while size :
                size -= 1
                temp = q.pop(0)
                if temp.left and temp.left.val == B or temp.right and temp.right.val == B:
                    found = True
                else:
                    if temp.left:
                        q.append(temp.left)
                    if temp.right:
                        q.append(temp.right)
            
        # weve got q :
        if found :
            for node in q :
                ans.append(node.val)
        return ans
        
