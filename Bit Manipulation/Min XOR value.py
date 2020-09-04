class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        A.sort()
        minn = float('inf')
        for i in range(len(A)-1):
            minn = min(minn,A[i]^A[i+1])
        
        return minn

# Optimal Method O(n) uses Trie
# Refer : https://www.geeksforgeeks.org/minimum-xor-value-pair/
