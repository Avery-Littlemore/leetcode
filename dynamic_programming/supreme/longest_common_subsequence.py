# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without 
# changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

# Example 1:
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.

# Example 2:
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.

# Example 3:
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
 

# Constraints:
# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.

"""
Return 0 if no common subsequence

Input: text1 = "abcde", text2 = "ace" 
Output: 3  

Input: text1 = "abc", text2 = "abc"
Output: 3

Input: text1 = "abc", text2 = "def"
Output: 0



abcde
l

ace
l

abcde

zcezcde

"""

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        p1 = len(text1) - 1
        p2 = len(text2) - 1
        cache = {}

        def helper(p1, p2):
            if p1 < 0 or p2 < 0:
                return 0
            if text1[p1] == text2[p2]:
                if (p1 - 1, p2 - 1) in cache:
                    return 1 + cache[(p1 - 1, p2 - 1)]
                else:
                    cache[(p1 - 1, p2 - 1)] = helper(p1 - 1, p2 - 1)
                    return 1 + cache[(p1 - 1, p2 - 1)]
            else:
                if (p1, p2 - 1) not in cache:
                    cache[(p1, p2 - 1)] = helper(p1, p2 - 1)
                if (p1 - 2, p2) not in cache:
                    cache[(p1 - 1, p2)] = helper(p1 - 1, p2)
                    
                return max(cache[(p1, p2 - 1)], cache[(p1 - 1, p2)])
        
        return helper(p1, p2)