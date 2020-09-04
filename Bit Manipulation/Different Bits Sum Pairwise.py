class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        n = len(A)
        ans = 0
        mod = 10**9+7
        for i in range(32):
            count = 0
            for e in A :
                if e & 1 << i :
                    count += 1
            
            ans += (count*(n-count)*2)%mod
        
        return ans%(mod)
