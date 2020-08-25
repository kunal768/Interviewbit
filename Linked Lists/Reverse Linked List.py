public class Solution {
    public ListNode reverseList(ListNode A) {
        if(A == null||A.next == null){
            return A;
        }
        
        ListNode prev = null;
        ListNode temp = null;
        ListNode curr = A;
        while(curr != null){
            temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }
        return prev;
        
    }
}
