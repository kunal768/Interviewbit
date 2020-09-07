class Solution:
	# @param A : integer
	# @return an integer
	def fibsum(self, A):
	    fib = [1,1]
	    i = 2
	    while fib[i-1] < A :
	        fib.append(fib[i-1]+fib[i-2])
	        i += 1
	    ans = 0 
	    n = len(fib)-1
	    while A > 0 :
	        while fib[n] > A:
	            n -= 1
	        A = A - fib[n]
	        ans += 1
	    return ans
