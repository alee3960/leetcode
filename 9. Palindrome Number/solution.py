class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Returns if the number x is a pajlindrome"""
        r = 0 # the reversed number
        o = x # the original number

        if x < 0: return False

        while x > 0:
            r = r * 10 + x % 10 # add last digit of x onto r
            x //= 10

        return o == r
    