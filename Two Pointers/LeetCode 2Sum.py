class Solution:
    def twoSum(self, a: List[int], target: int) -> List[int]:
        nums = sorted(a)
        l,h = 0,len(nums)-1
        while l < h:
            summ = nums[l] + nums[h]
            if summ == target:
                break
            if summ > target :
                h -= 1
            else:
                l += 1
        ans = []
        for i in range(len(a)):
            if nums[l] == a[i] :
                ans.append(i)
            elif nums[h] == a[i]:
                ans.append(i)
        return ans
