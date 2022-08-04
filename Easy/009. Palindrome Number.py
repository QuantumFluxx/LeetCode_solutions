class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1 = x
        return True if str(x)[::-1] == str(x1) else False