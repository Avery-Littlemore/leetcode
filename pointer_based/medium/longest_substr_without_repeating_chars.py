# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


# "dvdf"

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_table = {}
        total = 0
        max_found = 0
        anchor = 0
        runner = 0

        while runner < len(s):
            if hash_table.get(s[runner]):
                while s[anchor] != s[runner]:
                    del hash_table[s[anchor]]
                    anchor += 1
                    total -= 1
                hash_table[s[runner]] = True
                anchor += 1
            else:
                hash_table[s[runner]] = True
                total += 1
                if total > max_found:
                    max_found = total

            runner += 1

        return max_found

