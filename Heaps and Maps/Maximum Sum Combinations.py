from heapq import heappush,heappop
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        n = len(A)
        if C > n :
            return []
        A.sort()
        B.sort()
        pq = [(-(A[-1]+B[-1]),n-1,n-1)]
        ans = []
        vis = set({(n-1,n-1)})
        for _ in range(C):
            summ,i,j = heappop(pq)
            ans.append(-summ)
            if not (i-1,j) in vis :
                vis.add((i-1,j))
                heappush(pq,(-A[i-1]-B[j],i-1,j))
            if not (i,j-1) in vis :
                vis.add((i,j-1))
                heappush(pq,(-A[i]-B[j-1],i,j-1))
            
        return ans
            
            
            
            
