class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return (s[left:right - 1] == s[right - 1: left: -1]) or (s[left + 1:right] == s[right: left + 1: -1])
            left += 1
            right -= 1
        return True