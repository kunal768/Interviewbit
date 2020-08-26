# cram this algorithm 
mod = 1000003
def fact(n):
    if n == 0 :
        return 1
    return (n * fact(n-1))%mod

class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        n,ans = len(A),0
        mod = 1000003
        for i in range(n-1):
            c = 0
            for j in range(i+1,n):
                if A[j] < A[i] :
                    c += 1
            
            ans += (c*fact(n-i-1))%mod
        return (ans+1)%mod
