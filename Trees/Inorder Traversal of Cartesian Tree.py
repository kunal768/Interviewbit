class Solution:
	# @param A : list of integers
	# @return the root node in the tree
	def buildTree(self, A):
	    def findmax(start,end):
	        maxx = A[start]
	        index = start
	        for i in range(start,end+1):
	            if maxx<A[i]:
	                maxx = A[i]
	                index = i
	        return index
	       
	    def construct(start,end):
	        if start > end :
	            return 
	        maxindex = findmax(start,end)
	        root = TreeNode(A[maxindex])
	        root.left = construct(start,maxindex-1)
	        root.right = construct(maxindex+1,end)
	        return root
	    return construct(0,len(A)-1)
