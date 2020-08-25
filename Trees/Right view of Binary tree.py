class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        q = [A]
        ans = []
        while q :
            size = len(q)
            while size > 1 :
                size -= 1
                temp = q.pop(0)
                if temp.left :
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            temp = q.pop(0)
            ans.append(temp.val)
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        return ans
            
