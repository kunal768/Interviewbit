# Without Extra Space 
'''
Two constraints apply for balanced brackets:

    Same number of opening and closing brackets,
    You never close more brackets than you open.

'''
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        o = 0
        for i in A :
            if i == '(':
                o += 1
            else:
                o -= 1
            if o < 0 :
                return 0 
        return int(o == 0)

# Extra Space (Easy and Intuition Based)
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        stack = []
        for i in A :
            if not stack and i == ')':
                return 0 
            if stack and i == ')':
                stack.pop()
            else:
                stack.append(i)
        
        if stack :
            return 0 
        return 1
 
 
 
 
