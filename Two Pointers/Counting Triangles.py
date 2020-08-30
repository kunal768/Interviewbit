# Again Two Pointers with some variation 
# Check Out : https://www.geeksforgeeks.org/find-number-of-triangles-possible/

class Solution:
	# @param A : list of integers
	# @return an integer
	def nTriang(self, A):
	    count = 0
	    nums = sorted(A)
	    for i in range(len(nums)-1,0,-1):
	        l,h = 0,i-1
            while l < h :
                if nums[l] + nums[h] > nums[i]:
                    count += h-l
                    h -= 1
                else:
                    l += 1
        return count%(10**9+7)
                
