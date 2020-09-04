from heapq import heappush,heappop
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        if B > n :
            return []
        ans = []
        pq = []
        for i in A:
            heappush(pq,-i)
        
        for _ in range(B):
            ans.append(-heappop(pq))
        return ans
