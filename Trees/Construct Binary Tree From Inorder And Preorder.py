class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, preorder, inorder):
        instart,inend,prestart,preend = 0,len(inorder)-1,0,len(preorder)-1
        def construct(instart,inend,prestart,preend):
            if prestart > preend or instart > inend:
                return 
            
            root = TreeNode(preorder[prestart])
            k = 0
            for idx,val in enumerate(inorder):
                if preorder[prestart] == val:
                    k = idx
                    break
            root.left = construct(instart,k-1,prestart+1,prestart+(k-instart))
            root.right = construct(k+1,inend,prestart+(k-instart)+1,preend)
            return root
        
        return construct(instart,inend,prestart,preend)


# Run this code 
''' 
public class Solution {

    public TreeNode buildTree(int[] preorder, int[] inorder) {
    int preStart = 0;
    int preEnd = preorder.length-1;
    int inStart = 0;
    int inEnd = inorder.length-1;
 
    return construct(preorder, preStart, preEnd, inorder, inStart, inEnd);
    }
        public TreeNode construct(int[] preorder, int preStart, int preEnd, int[] inorder, int inStart, int inEnd){
    if(preStart>preEnd||inStart>inEnd){
        return null;
    }
 
    int val = preorder[preStart];
    TreeNode p = new TreeNode(val);
 
    //find parent element index from inorder
    int k=0;
    for(int i=0; i<inorder.length; i++){
        if(val == inorder[i]){
            k=i;
            break;
        }
    }
 
    p.left = construct(preorder, preStart+1, preStart+(k-inStart), inorder, inStart, k-1);
    p.right= construct(preorder, preStart+(k-inStart)+1, preEnd, inorder, k+1 , inEnd);
 
    return p;
}
    
}
'''
