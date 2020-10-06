class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, s, numRows):
        ans = ""
        if numRows == 1:
            return s
        size = min(numRows, len(s))
        hm = {i : [] for i in range(size)}
        down = False
        curr_row = 0 
        for c in s :
            hm[curr_row].append(c)
            if curr_row == 0 or curr_row == size - 1 :
                down = not down 
            curr_row += 1 if down else -1
        
        for i in range(size):
            ans += "".join(hm[i])
        return ans
