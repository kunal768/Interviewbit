from collections import defaultdict
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        n = len(A)
        if B > n:
            return []
        
        dc,hm = 0,defaultdict(lambda : 0)
        for i in range(B):
            if hm[A[i]] == 0 :
                dc += 1
            hm[A[i]] += 1
        
        ans = [dc]
        for i in range(B,n):
            if hm[A[i-B]] == 1 :
                dc -= 1
            hm[A[i-B]] -= 1    
            
            if hm[A[i]] == 0 :
                dc += 1
            hm[A[i]] += 1
            
            ans.append(dc)
        
        return ans
            
  
