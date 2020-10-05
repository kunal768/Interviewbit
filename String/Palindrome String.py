class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        ans = ''
        for i in A :
            if i.isalnum():
                ans += i.lower()
        return int(ans == ans[::-1])
