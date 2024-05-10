# Given an array arr of integers, check if there exist two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]
 
# Example 1:
# Input: arr = [10,2,5,3]
# Output: true
# Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

# Example 2:
# Input: arr = [3,1,7,11]
# Output: false
# Explanation: There is no i and j that satisfy the conditions.

# Constraints:
# 2 <= arr.length <= 500
# -103 <= arr[i] <= 103

"""
P:
- given an array of integers, does there exist an integer that is equal to 2* another integer?
- if any one integer which is twice any other integer is found, return true
- if none are found, return false
- the integers can be equal, but the INDEXES cannot

Input: array of integers
Output: boolean

Edge cases: 
element is 0 -> add guard clause
element is negative -> doesn't matter

E: 
Input: arr = [10,2,5,3]
Output: true

Input: arr = [3,1,7,11]
Output: false

D:
- array as input
- potentially use a hash to store values and minimize time complexity
    - aim for O(N)

A:
- iterate through the array and store each value in the hash as a key
    - values are 1 if occurred once, etc

- iterate through the array again 
    - see if value * 2 exists in the hash
        - if so and element is 0, check if it occurred twice
            - if so, retrn True
        - else return True
- return false


"""

class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hash_table = {}
        for element in arr:
            if hash_table.get(element):
                hash_table[element] += 1
            else:
                hash_table[element] = 1
        
        for element in arr:
            if hash_table.get(element * 2):
                if element == 0:
                    if hash_table[element] > 1:
                        return True
                else:
                    return True
        
        return False
