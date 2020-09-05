from heapq import heappush,heappop
class Solution:
	# @param A : integer
	# @param B : list of integers
	# @return an integer
	def nchoc(self, A, B):
	    mod = 10**9+7
	    pq = []
	    for i in B :
	        heappush(pq,-i)
	    ans = 0
	    for _ in range(A):
	        temp = -heappop(pq)
	        heappush(pq,-(temp//2) )
	        ans += (temp%mod)
	    return ans%mod
	       
	        
