# Remember A^A = 0 
'''
we can observe that number at i-th index will have 
(i + 1) * (N - i) frequency. 
'''
# if no such pattern just calculate the freq manually
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        res = 0 
        for i in range(len(A)):
            freq = (i+1)*(len(A)-i)
            if freq & 1 :
                res ^= A[i]
        return res
            
