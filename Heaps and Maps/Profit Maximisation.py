from heapq import heappush,heappop
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        pq = []
        for i in A :
            heappush(pq,-i)
        ans = 0
        while B :
            temp = -heappop(pq)
            heappush(pq,-temp+1)
            ans += temp
            B -= 1
        return ans
            
            
            
            
