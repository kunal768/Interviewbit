from collections import defaultdict
class Solution:
	# @param A : root node of tree
	# @return a list of list of integers
	def verticalOrderTraversal(self, A):
	    if not A :
	        return []
	    hm = defaultdict(lambda : [])
	    q = [(A,0)]
            for node in q :
        	hm[node[1]].append(node[0].val)
	    	if node[0].left:
				q.append((node[0].left,node[1]-1))
	    	if node[0].right:
				q.append((node[0].right,node[1]+1))
	    return [hm[i] for i in sorted(hm)]
	    
