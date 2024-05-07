# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
# of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a 
# subsequence of "abcde" while "aec" is not).

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_counter = 0
        t_counter = 0
        while s_counter < len(s) and t_counter < len(t):
            if s[s_counter] == t[t_counter]:
                s_counter += 1
            t_counter += 1

        return s_counter == len(s)