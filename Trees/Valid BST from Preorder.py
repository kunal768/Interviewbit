class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # pehle saare number root se chote honge fir root se bade honge ye order break nhi hona chahiye
        stack = []
        root = float('-inf')
        for val in A :
            if val < root:
                return 0
            
            while stack and stack[-1] < val :
                root = stack.pop()
            stack.append(val)
        return 1
