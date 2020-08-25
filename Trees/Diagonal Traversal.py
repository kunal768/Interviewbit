# recursive (Time Exceeded) [the compiler is fucked up so implement the below solution in C++ aur tumhara chal jayega]
from collections import defaultdict
class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        if not A:
            return []
        hm = defaultdict(lambda : [])
        def dfs(node,d):
            if not node:
                return 
            nonlocal hm 
            hm[d].append(node.val)
            if node.left:
                dfs(node.left,d+1)
            if node.right:
                dfs(node.right,d)
        dfs(A,0) 
        ans = []
        for i in hm:
            ans.extend(hm[i])
        return ans
        
# iterative (Time Limit Exceeded) Ruko zara.. Sabar Karo 
class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        if not A:
            return []
        q = [A]
        ans = []
        while q :
            temp = q.pop(0)
            while temp :
                ans.append(temp.val)
                if temp.left:
                    q.append(temp.left)
                temp = temp.right
        return ans
        

  

  
