class Solution:
    # @param A : root node of tree
    # @return an integer
    def sumNumbers(self, A):
        mod = 1003
        ans = 0 
        def dfs(node,summ):
            if not node :
                return 
            nonlocal ans,mod
            # if leaf node
            # print(summ)
            if not node.left and not node.right:
                # update curr_sum
                summ += str(node.val)
                # contribute to ans 
                ans += int(summ)%mod
            dfs(node.left,summ+str(node.val))
            dfs(node.right,summ+str(node.val))
            
        dfs(A,"")
        return ans%mod
                
            
