class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        stack,vector = [],[]
        for i in range(len(A)):
            if not stack :
                vector.append(-1)
            elif stack and stack[-1] >= A[i]:
                while stack and stack[-1] >= A[i]:
                    stack.pop()
                if not stack :
                    vector.append(-1)
                else:
                    vector.append(stack[-1])
            elif stack and stack[-1] < A[i]:
                vector.append(stack[-1])
            stack.append(A[i])
            
        return vector
            
            
