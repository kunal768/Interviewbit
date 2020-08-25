# BForce approach of 2 sum in BFS (but accepted)
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def t2Sum(self, root, target):
        # for i in arr : is summ - i in hm return true else hm.add(i)
        if not root or (not root.left and not root.right) :
            return 0
        vis = set()
        q = [root]
        while q :
            for x in q :
                if target - x.val in vis :
                    return 1
                vis.add(x.val)
            q = [x for n in q for x in (n.left,n.right) if x]
            
        return 0
            
'''
https://www.geeksforgeeks.org/pair-with-a-given-sum-in-bst-set-2/?ref=rp

In this article, we will solve the same problem using a space efficient method by reducing the space complexity to O(H) where H is the height of BST. For that, we will use two pointer technique on BST. Thus, we will maintain a forward and a backward iterator that will iterate the BST in the order of in-order and reverse in-order traversal respectively. Following are the steps to solve the problem:

    Create a forward and backward iterator for BST. Let’s say the value of nodes they are pointing at are v1 and v2.
    Now at each step,
        If v1 + v2 = X, we found a pair.
        If v1 + v2 < x, we will make forward iterator point to the next element.
        If v1 + v2 > x, we will make backward iterator point to the previous element.
    If we find no such pair, answer will be “No”.

Below is the implementation of the above approach:        
'''
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def t2Sum(self, root, target):
        # for i in arr : is summ - i in hm return true else hm.add(i)
        if not root or (not root.left and not root.right) :
            return 0
        
        it1,it2 = [],[]
        
        c = root 
        while c :
            it1.append(c)
            c = c.left
        
        c = root
        while c:
            it2.append(c)
            c = c.right
        
        # two pointers
        while it1[-1] != it2[-1]:
            v1,v2 = it1[-1].val,it2[-1].val
            if v1+v2 == target:
                return 1
            
            # move forward iterator
            if v1+v2 < target :
                c = it1.pop().right
                while c :
                    it1.append(c)
                    c = c.left
            else:
                c = it2.pop().left
                while c:
                    it2.append(c)
                    c = c.right
        return 0
            
            
        


