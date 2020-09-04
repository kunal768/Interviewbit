# Handles only positive
from collections import defaultdict
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        f = defaultdict(lambda : 0)
        res = 0
        for i in range(32):
            for e in A :
                if e & 1 << i :
                    f[i] += 1
            
            res |= f[i]%3 << i
        return res
        

# Handles negative as well 
from collections import defaultdict
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        f = defaultdict(lambda : 0)
        for e in A :
            for i in range(32):
                if e & 1 << i :
                    f[i] += 1
        res = 0
        for i in range(32):
            if i == 31 and f[i]%3 :
                res -= 1 << 31 
            else:
                res |= f[i]%3 << i
        return res
            
