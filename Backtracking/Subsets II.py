class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(curr,rest):
            nonlocal res
            if not rest :
                if curr not in res :
                    res += [curr]
            
            else:
                dfs(curr,rest[1:])
                dfs(curr+[rest[0]],rest[1:])
        
        dfs([],sorted(nums))
        return sorted(res)
