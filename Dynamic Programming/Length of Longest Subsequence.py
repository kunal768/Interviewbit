class Solution:
	# @param A : tuple of integers
	# @return an integer
	def longestSubsequenceLength(self, A):
	    n = len(A)
	    dp1 = [1]*n
	    for i in range(1,n):
	        for j in range(i):
	            if A[i] > A[j] and dp1[i] < dp1[j] + 1:
	                dp1[i] = dp1[j] + 1
	    
	    dp2 = [1]*n
	    for i in range(n-2,-1,-1):
	        for j in range(n-1,i,-1):
	            if A[i] > A[j] and dp2[i] < dp2[j] + 1 :
	                dp2[i] = dp2[j] + 1
	    
	    ans = 0 
	    for i in range(n):
	        ans = max(ans,dp1[i]+dp2[i]-1)
	    return ans
	    
	   
	   
