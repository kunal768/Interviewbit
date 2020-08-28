class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, path):
        path = path.split("/")
        stack = []
        for x in path :
            if x :
                if x == '..':
                    try :
                        stack.pop()
                    except :
                        stack = []
                elif x != '.':
                    stack.append(x)
                    
        return "/"+"/".join(stack)
                    
