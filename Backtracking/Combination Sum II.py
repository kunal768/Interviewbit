class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        n = len(A)
        ans = []
        A.sort()
        def dfs(ans,path,index,n):
            if sum(path) > B :
                return 
            if sum(path) == B :
                if not path in ans :
                    ans.append(path)
                return 
            
            for i in range(index,n):
                dfs(ans,path+[A[i]],i+1,n)
                dfs(ans,path,i+1,n)
        
        dfs(ans,[],0,n)
        return ans
