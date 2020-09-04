from heapq import heappush,heappop
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        A.sort()
        B.sort()
        n = len(A)
        if n <= 0 :
            return []
        pq = []
        heappush(pq,( -(A[n-1]+B[n-1]),n-1,n-1))
        ans = []
        vis = set({(n-1,n-1)})
        for _ in range(n):
            summ,i,j = heappop(pq)
            ans.append(-summ)
            if not ((i-1,j)) in vis :
                vis.add((i-1,j))
                heappush(pq,( -(A[i-1]+B[j]),i-1,j))
            
            if not ((i,j-1)) in vis :
                vis.add((i,j-1)) 
                heappush(pq,(-(A[i]+B[j-1]),i,j-1))
        return ans
            
