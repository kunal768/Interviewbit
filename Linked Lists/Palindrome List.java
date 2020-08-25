// Bad Method : (Stack) extra space + Two Pass
public class Solution {
    public int lPalin(ListNode A) {
        Stack<Integer>stack = new Stack<Integer>();
        ListNode temp = A;
        while(temp != null){
            stack.push(temp.val);
            temp = temp.next;
        }
        
        while(A != null){
            if(A.val != stack.peek()){
                return 0;
            }
            if(!stack.empty() && A ==null){
                return 0;
            }
            else if(stack.empty() && A != null){
                return 0;
            }
            if (stack != null)
                stack.pop();
            A = A.next;
        }
        return 1;
    }
}


// Good Method 
