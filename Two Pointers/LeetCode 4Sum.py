# -- Note : To whoever  reading this, you can follow my two pointers and target sum template.
# -- Go to https://leetcode.com/problems/3sum/discuss/820254/Two-Pointers-Python3-AC : my template


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        A = sorted(nums)
        ans = []
        n = len(nums)
        for i in range(n-3):
            for j in range(i+1,n-2):
                l,h = j+1,len(A)-1
                while l<h :
                    summ = A[i] + A[j] + A[l] +A[h]
                    if summ == target :
                        ans.append((A[i],A[j],A[l],A[h]))
                    if summ > target :
                        h -= 1
                    else :
                        l += 1
        return map(list,list(set(ans)))
        

