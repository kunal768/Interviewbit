# https://www.geeksforgeeks.org/python-handling-recursion-limit/

from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, n, B):
        B.sort(key = lambda x : x[2])
        parent = defaultdict(lambda : -1)

        def find_parent(x):
            nonlocal parent
            if parent[x] == -1:
                return x
            return find_parent(parent[x])
        
        ans = 0
        for i in range(len(B)):
            u,v = find_parent(B[i][0]),find_parent(B[i][1])
            if u != v :
                parent[u] = v
                ans += B[i][2]

        return ans
                
        
            
        
        
        
        
            
            
