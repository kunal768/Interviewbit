# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from heapq import heappush,heappop
class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        pq = []
        for node in A :
            while node :
                heappush(pq,node.val)
                node = node.next
        
        L = ListNode(0)
        temp = L
        while pq :
            temp.next = ListNode(heappop(pq))
            temp = temp.next
        
        return L.next
        
        
