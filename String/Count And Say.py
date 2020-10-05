from itertools import groupby 
class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        ans = ""
        start = "1"
        for _ in range(1, A):
            curr = ""
            for key, grp in groupby(start):
                curr += str(len(list(grp)))+key
            start = curr 
        return start
            
                
