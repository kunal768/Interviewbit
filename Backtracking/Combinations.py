class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def combine(self, n, k):
        A = [i for i in range(1,n+1)]
        ans = []
        def dfs(path,index):
            nonlocal ans
            if index == n :
                if len(path) == k :
                    if not path in ans :
                        ans.append(path)
                    return 
            for i in range(index,n):
                dfs(path+[A[i]],i+1)
                dfs(path,i+1)
        
        dfs([],0)
        return ans
                
            
        
