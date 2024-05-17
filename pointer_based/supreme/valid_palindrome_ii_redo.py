# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# Example 1:
# Input: s = "aba"
# Output: true

# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.

# Example 3:
# Input: s = "abc"
# Output: false

class Solution(object):
    def validPalindrome(self, s):
        def helper(start, end):
            if end <= start:
                return True
            
            if s[start] == s[end]:
                return helper(start + 1, end - 1)
            else:
                return False
            
        start = 0
        end = len(s) - 1
        while end > start:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return helper(start + 1, end) or helper(start, end - 1)
            
        return True
