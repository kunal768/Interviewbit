class Solution:
	# @param A : list of strings
	# @return a strings
	def longestCommonPrefix(self, A):
	    lcp = A[0]
	    for i in range(1,len(A)):
	        while lcp not in A[i]:
	            lcp = lcp[:-1]
	            if not lcp :
	                return ""
	            if lcp in A[i]:
	                while A[i].index(lcp) != 0 :
	                    lcp = lcp[:-1]
	    return lcp 
