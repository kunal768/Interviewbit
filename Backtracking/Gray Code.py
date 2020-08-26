# size of gray code sequence of n is 2^n
# gray code of x is x^x>>1
class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = []
        x = 0 
        size = 2**n
        while len(ans) < size :
            ans.append(x^x>>1)
            x += 1
        return ans
