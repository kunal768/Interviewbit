class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        ans = []
        # removing leading spaces
        i = 0 
        while i < len(A) and A[i] == ' ':
            i += 1
        
        # handle whitespaces 
        while i < len(A) :
            new = ""
            while i < len(A) and A[i] != ' ':
                new += A[i]
                i += 1
            
            ans.append(new)
            while i < len(A) and A[i] == ' ':
                i += 1
        
        # reverse list
        l, h = 0, len(ans)-1
        while l < h :
            ans[l], ans[h] = ans[h], ans[l]
            l += 1
            h -= 1
        
        # construct string 
        return ' '.join(ans)

