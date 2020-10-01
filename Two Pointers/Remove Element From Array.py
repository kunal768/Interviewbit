class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, nums, target):
        count = 0 
        for i in range(len(nums)):
            if nums[i] != target :
                nums[count] = nums[i]
                count += 1
        return count
