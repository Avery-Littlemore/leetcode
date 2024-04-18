# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# time complexity of O(N + M) ~= O(N)
# space complexity of O(N)

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        hash_table = {}
        for char in s:
            if hash_table.get(char):
                hash_table[char] += 1
            else:
                hash_table[char] = 1

        for char in t:
            if hash_table.get(char):
                hash_table[char] -= 1
            else:
                return False
            
        return True

        """
        :type s: str
        :type t: str
        :rtype: bool
        """