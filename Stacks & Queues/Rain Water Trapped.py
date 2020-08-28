class Solution:
	# @param A : tuple of integers
	# @return an integer
	def trap(self, A):
	    n = len(A)
	    l,r = [0]*n,[0]*n
	    l[0] = A[0]
	    for i in range(1,n):
	        l[i] = max(A[i],l[i-1])
	    
	    r[-1] = A[-1]
	    for i in range(n-2,-1,-1):
	        r[i] = max(A[i],r[i+1])
	       
	   # print(l,r)
	    maxx = 0
	    for i in range(n):
	        maxx += min(l[i],r[i])-A[i]
	    return maxx
	        
	        
	        
