class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        def construct(start,end):
            if start > end :
                return 
            mid = (start+end)//2
            root = TreeNode(A[mid])
            root.left = construct(start,mid-1)
            root.right = construct(mid+1,end)
            return root
        return construct(0,len(A)-1)
