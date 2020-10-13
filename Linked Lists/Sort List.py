# Only iterative merge works on Interviewbit, the recursive one works on LeetCode
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None
def merge(A, B):
    if not A or not B :
        return A or B 
    new = ListNode(-1)
    temp = new
    l, r = A, B
    while l and r :
        if l.val <= r.val :
            temp.next = l
            l = l.next
        else:
            temp.next = r
            r = r.next
        
        temp = temp.next
    
    while l :
        temp.next = l 
        l = l.next
        temp = temp.next
    
    while r :
        temp.next = r
        r = r.next
        temp = temp.next
    
    return new.next
    
    
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        if not A or not A.next:
            return A
        s, f, p = A, A, None
        while s and f and f.next:
            p = s
            s = s.next
            f = f.next.next
        
        p.next = None
        l, r = self.sortList(A), self.sortList(s)
        return merge(l, r)
        
        
        
        
