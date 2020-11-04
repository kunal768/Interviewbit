class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        fb, fs, sb, ss = float('inf'), 0, float('inf'), 0 
        for price in A :
            fb = min(fb, price)
            fs = max(fs, price - fb)
            sb = min(sb, price - fs)
            ss = max(ss, price - sb)
        
        return ss
