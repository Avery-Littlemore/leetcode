# Given a string s which represents an expression, evaluate this expression and return its value. 

# The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# Example 1:

# Input: s = "3+2*2"
# Output: 7

# Example 2:
# Input: s = " 3/2 "
# Output: 1

# Example 3:
# Input: s = " 3+5 / 2 "
# Output: 5

# Constraints:
# 1 <= s.length <= 3 * 105
# s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
# s represents a valid expression.
# All the integers in the expression are non-negative integers in the range [0, 231 - 1].
# The answer is guaranteed to fit in a 32-bit integer.

"""
3 + 2 + 5 * 6 - 1 + 8 / 4

5

"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []

        operation = '+'
        current_num = 0
        for i in range(len(s)):
            if s[i].isdigit():
                current_num = current_num * 10 + int(s[i])
            if s[i] in '+-*/' or i == len(s) - 1:
                if operation == '+':
                    stack.append(current_num)
                elif operation == '-':
                    stack.append(-current_num)
                elif operation == '*':
                    stack.append(stack.pop() * current_num)
                elif operation == '/':
                    temp = stack.pop()
                    if temp // current_num < 0 and temp % current_num != 0:
                        stack.append(temp // current_num + 1)
                    else:    
                        stack.append(temp // current_num)
                    
                    # in one line, to replace lines 58-61 -> ONLY WORKS IN PYTHON3
                    # stack.append(math.trunc(temp/current_num))

                current_num = 0
                operation = s[i]
        return sum(stack)