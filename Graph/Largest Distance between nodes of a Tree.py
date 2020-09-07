from collections import defaultdict
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        g = defaultdict(lambda : [])
        n = len(A)
        for i in range(n):
            if A[i] != -1 :
                g[i].append(A[i])
                g[A[i]].append(i)
                
        def bfs(q,vis):
            nonlocal g
            maxx = float('-inf')
            farthest = 0 
            while q :
                node,d = q.pop(0)
                if d > maxx :
                    maxx = d
                    farthest = node 
                vis[node] = 1
                for adj in g[node]:
                    if not vis[adj]:
                        q.append((adj,d+1))
            return maxx,farthest
            

        q = [(0,0)]
        vis = [0]*n
        maxx,farthest = bfs(q,vis)
        vis = [0]*n
        q = [(farthest,0)]
        maxx,f2 = bfs(q,vis)
        return maxx
        
                
                
                
                
            
