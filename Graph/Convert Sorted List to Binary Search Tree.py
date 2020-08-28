# -- You Can Some Times Brute Force Things

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the root node in the tree
    def sortedListToBST(self, A):
        arr = []
        while A :
            arr.append(A.val)
            A = A.next
            
        if len(arr) == 1:
            return TreeNode(arr[0])
        
        # print
        
        def construct(l,h,arr):
            if l > h :
                return
            mid = (l+h)//2
            root = TreeNode(arr[mid])
            root.left = construct(l,mid-1,arr)
            root.right = construct(mid+1,h,arr)
            return root
        
        return construct(0,len(arr)-1,arr)
        
