class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        A.sort()
        ans = []
        for i in range(len(A)-2):
            l,h = i+1,len(A)-1
            if i > 0 and A[i] == A[i-1]:
                continue
            while l < h :
                summ = A[i]+A[l]+A[h]
                if summ == 0 :
                    temp = [A[i],A[l],A[h]]
                    if ans and ans[-1] == temp :
                        pass
                    else :
                        ans.append((A[i],A[l],A[h]))
                    l += 1
                    h -= 1
                elif summ > 0 :
                    h -= 1
                else:
                    l += 1
        return ans
