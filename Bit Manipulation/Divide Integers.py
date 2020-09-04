class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def divide(self, A, B):
        mod = 2**31 -1
        sign = -1 if (A<0)^(B<0) else 1
        A = abs(A)
        B = abs(B)
        q,t = 0,0
        for i in range(31,-1,-1):
            if t + (B << i) <= A :
                t += B << i
                q |= 1 << i
        if sign*q >= mod :
            return mod
        return sign*q
            
