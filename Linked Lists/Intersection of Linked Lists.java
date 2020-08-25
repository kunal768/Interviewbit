/**
 * Definition for singly-linked list.
 * class ListNode {
 *     public int val;
 *     public ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
 // O(1) space
 
public class Solution {
	public ListNode getIntersectionNode(ListNode a, ListNode b) {
	    if(a == null && b == null){
	        return a;
	    }
	    if(a == null || b == null){
	        return null;
	    }
	    
	    ListNode tempa = a;
	    ListNode tempb = b;
	    int ac = 0; int bc = 0;
	    while(tempa != null){
	        tempa = tempa.next;
	        ac++;
	    }
	    while(tempb != null){
	        tempb = tempb.next;
	        bc++;
	    }
	    
	    int d = Math.abs(bc-ac);
	    if(ac > bc){
	        while((d != 0 )&& (a != null)){
	            a = a.next;
	            d--;
	        }
	    }
	    else if(ac < bc){
	        while((d!=0) && (b!=null)){
	            b = b.next;
	            d--;
	        }
	    }
	   
	   while((a != null) && (b!=null)){
	       if (a == b){
	           return a;
	       }
	       a = a.next;
	       b = b.next;
	   } 
	   
	   return null; 
	}
}
