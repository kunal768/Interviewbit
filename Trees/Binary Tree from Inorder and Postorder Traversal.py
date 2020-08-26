class Solution:
	def buildTree(self, inorder, postorder):
		def construct(instart,inend,poststart,postend):
		    if poststart > postend or instart > inend :
		        return 
		    root = TreeNode(postorder[postend])
		    k = inorder.index(postorder[postend])
		    root.left = construct(instart,k-1,poststart,poststart+k-instart-1)
		    root.right = construct(k+1,inend,poststart+k-instart,postend-1)
		    return root
		return construct(0,len(inorder)-1,0,len(postorder)-1)
	   
 '''
  -- Java Solution

public class Solution {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        	if (inorder == null || postorder == null || inorder.length != postorder.length)
		return null;
	HashMap<Integer, Integer> hm = new HashMap<Integer,Integer>();
	for (int i=0;i<inorder.length;++i)
		hm.put(inorder[i], i);
	return buildTreePostIn(inorder, 0, inorder.length-1, postorder, 0, 
                          postorder.length-1,hm);
    }
    private TreeNode buildTreePostIn(int[] inorder, int is, int ie, int[] postorder, int ps, int pe, 
                                 HashMap<Integer,Integer> hm){
	if (ps>pe || is>ie) return null;
	TreeNode root = new TreeNode(postorder[pe]);
	int ri = hm.get(postorder[pe]);
	TreeNode leftchild = buildTreePostIn(inorder, is, ri-1, postorder, ps, ps+ri-is-1, hm);
	TreeNode rightchild = buildTreePostIn(inorder,ri+1, ie, postorder, ps+ri-is, pe-1, hm);
	root.left = leftchild;
	root.right = rightchild;
	return root;
}
    
}
'''
	        
