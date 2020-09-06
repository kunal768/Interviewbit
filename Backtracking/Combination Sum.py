class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A.sort()
        ans = []
        n = len(A)
        def dfs(path,index):
            nonlocal ans,n
            if sum(path) > B :
                return 
            if sum(path) == B or index >= n :
                if not path in ans :
                    ans.append(path)
                return 
            
            for i in range(index,n):
                dfs(path+[A[i]],i)
                
        dfs([],0)
        return ans
        
        
