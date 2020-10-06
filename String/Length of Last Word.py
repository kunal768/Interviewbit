class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        if not A :
            return 0
        last = len(A)-1
        while last >= 0 :
            while last >= 0 and A[last] == ' ':
                last -= 1
            
            count = 0 
            while last >= 0 and A[last] != ' ':
                count += 1
                last -= 1
            
            return count 
        
        
            
