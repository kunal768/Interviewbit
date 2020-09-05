from heapq import heappush,heappop
class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        ans = []
        pq = []
        for row in A :
            for num in row :
                heappush(pq,num)
        while pq :
            ans.append(heappop(pq))
        return ans
