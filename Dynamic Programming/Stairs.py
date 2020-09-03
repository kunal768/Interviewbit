from functools import lru_cache
class Solution:
	# @param A : integer
	# @return an integer
	def climbStairs(self, A):
	    @lru_cache(None)
	    def dfs(A):
	        if A <=  1:
	            return 1 
	        return dfs(A-1)+dfs(A-2)
	    return dfs(A)
