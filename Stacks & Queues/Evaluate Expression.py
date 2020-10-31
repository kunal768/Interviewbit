class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack = []
        symbols = {"*","+","-","/"}
        for x in A :
            if not stack and not x in symbols :
                stack.append(int(x))
            
            if not x in symbols :
                stack.append(int(x))
            elif x in symbols :
                if len(stack) > 1 :
                    a, b = stack.pop(), stack.pop()
                    if x == '*' :
                        stack.append(a*b)
                    elif x == '+':
                        stack.append(a+b)
                    
                    elif x == '-':
                        stack.append(b - a)
                    
                    elif x == '/':
                        stack.append(b//a)
            
        # print(stack)
        return stack[-1] if stack else 0
            
                    
