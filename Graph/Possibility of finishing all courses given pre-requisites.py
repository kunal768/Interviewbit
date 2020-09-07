# Kahn's Topological Sorting Algorithm Refer : https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/
from collections import defaultdict
class Solution:
	# @param A : integer
	# @param B : list of integers
	# @param C : list of integers
	# @return an integer
	def solve(self, A, B, C):
	    n = A
	    g = defaultdict(lambda : [])
	    inn = [0]*n
	    for i in range(len(B)):
	        g[B[i]].append(C[i])
	        inn[C[i]-1] += 1
	    q = []
	    for i in range(n):
	        if inn[i] == 0 :
	            q.append(i)
	    cnt = 0
	    order = []
	    while q :
	        node = q.pop(0)
	        order.append(node+1)
	        for adj in g[node+1]:
	            inn[adj-1] -= 1
	            if inn[adj-1] == 0 :
	                q.append(adj-1)
	        cnt += 1
	    
	    if cnt != n or len(order) == 0:
	        return 0
	            
	    return 1
	        
	        
