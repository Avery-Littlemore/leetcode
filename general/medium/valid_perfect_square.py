# Given a positive integer num, return true if num is a perfect square or false otherwise.

# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

# You must not use any built-in library function, such as sqrt.

# Example 1:
# Input: num = 16
# Output: true
# Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

# Example 2:
# Input: num = 14
# Output: false
# Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

# Constraints:
# 1 <= num <= 2^31 - 1

"""
P:
- take a num as input
- return true if the number is a perfect square
- else return false

E:
16 -> True
14 -> False
9 -> True
25 -> True
1 -> True
0 -> True

D:
input is integer
output boolean
Consider O(N) time comp to read through every integer below num to see if it is the square root
Is there a better solution...
    Binary search-like method?

A:
- edge cases: if number is 0 or 1, return True
- create variable upper_limit and set it to num
- create variable pivot and set it to half of num (int division)
- create variable lower_limit and set it to 0
- while upper_limit is more than 1 whole number higher than pivot
    - if pivot squared is greater than num
        - set upper_limit to pivot
    - else if pivot squared is less than num
        - set lower_limit to pivot
    - else
        return true
    - set pivot to halfway point between lower_limit and upper_limit

Time comp: O(log N)
Space comp: O(1)

"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0 or num == 1:
            return True
        
        upper_limit = num
        lower_limit = 0
        pivot = num // 2

        while upper_limit - lower_limit > 1:
            if pivot**2 > num:
                upper_limit = pivot
            elif pivot**2 < num:
                lower_limit = pivot
            else:
                return True
            pivot = upper_limit - (upper_limit - lower_limit) // 2
        
        return False
        

# def isPerfectSquare(num):
#     """
#     :type num: int
#     :rtype: bool
#     """
#     if num == 0 or num == 1:
#             return True
        
#     upper_limit = num
#     lower_limit = 0
#     pivot = num // 2
#     counter = 0

#     while upper_limit - lower_limit > 1 and counter < 10:
#         if pivot**2 > num:
#             upper_limit = pivot
#         elif pivot**2 < num:
#             lower_limit = pivot
#         else:
#             return True
#         pivot = upper_limit - (upper_limit - lower_limit) // 2
#         counter += 1
    
#     return False
        
# print(isPerfectSquare(14))
# # UPPER     PIVOT   LOWER   RESULT
# # 14        7       0       TOO HIGH
# # 7         3       0       TOO LOW
# # 7         5       3       TOO HIGH
# # 5         4       3       TOO HIGH
# # 4         3       3       TOO LOW
# # break

# print(isPerfectSquare(16))
# print(isPerfectSquare(25))
# print(isPerfectSquare(9))
# print(isPerfectSquare(2))
# print(isPerfectSquare(1))
# print(isPerfectSquare(0))