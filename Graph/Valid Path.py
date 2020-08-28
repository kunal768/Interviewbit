class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : list of integers
    # @param F : list of integers
    # @return a strings
    def solve(self, tx, ty, n, R,E,F):
        centers = [x for x in zip(E,F)]
        vis = [[0 for _ in range(ty+1)] for _ in range(tx+1)]
        def out_of_circles(x,y):
            nonlocal centers
            for center in centers :
                if (x-center[0])**2 + (y-center[1])**2 <= R*R :
                    return False
            return True
        
        def issafe(x,y):
            return x >= 0 and x <= tx and y >= 0 and y <= ty and out_of_circles(x,y)
        q = [(0,0)]
        vis[0][0] = 1
        while q :
            x,y = q.pop(0)
            if x == tx and y == ty :
                return "YES"
            for i in { (-1,0),(1,0),(0,1),(0,-1),(-1,1),(1,1),(-1,-1),(1,-1)} :
                ax,ay = x + i[0],y+i[1]
                if issafe(ax,ay) and not vis[ax][ay]:
                    vis[ax][ay] = 1
                    q.append((ax,ay))
            
        return "NO"
        
        
        
        
        
        
        
        
        
