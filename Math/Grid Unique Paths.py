from functools import lru_cache
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        @lru_cache(None)
        def count(x,y):
            if x == 0 or y == 0 :
                return 1
            return count(x-1,y)+count(x,y-1)
        return count(A-1,B-1)
