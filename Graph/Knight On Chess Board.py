class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @param F : integer
    # @return an integer
    def knight(self, A, B, C, D, E, F):
        n,m = A,B
        q = [(C-1,D-1,0)] 
        poss = {(-2,-1),(-2,1),(2,1),(2,-1),(1,2),(-1,2),(-1,-2),(1,-2)}
        vis = [[0 for _ in range(m)] for _ in range(n)]
        def issafe(x,y):
            return x>= 0 and x < n and y >= 0 and y < m and not vis[x][y]
        
        while q:
            x,y,d = q.pop(0)
            vis[x][y] = 1
            if x == E-1 and y == F-1 :
                return d
            for i in poss :
                ax,ay = x+i[0],y+i[1]
                if issafe(ax,ay):
                    q.append((ax,ay,d+1))
                    vis[ax][ay] = 1
        return -1
