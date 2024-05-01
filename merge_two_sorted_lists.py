# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]


# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

"""
P:
- take as input two (heads of sorted linked) lists
- merge the lists into one sorted list
- return the head of the sorted list

- edge cases:
    - empty lists
    - single-item lists
    - repeated nums (any order is fine)

- mutate the list with the lower first value

E:
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

D:
- linked lists per ListNode below

A:
- if not list1
    - return list2
- if not list2
    - return list1

- if list1 val <= list2 val
    - merged_list = list1
    - other_list = list2
- else
    - merged_list = list2
    - other_list = list1
- while merged_list.next and other_list
    - if merged_list.next val == merged_list val
        - merged_list = merged_list.next
    - else if merged_list.next.val > other_list.val
        - [merged_list.next, other_list] = [other_list, merged_list.next]
- if other_list
    - merged_list.next = other_list
- return merged_list

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            curr_list = list1
            other_list = list2
        else:
            curr_list = list2
            other_list = list1

        head = curr_list

        while curr_list.next and other_list:
            if curr_list.next.val == curr_list.val or curr_list.next.val <= other_list.val:
                curr_list = curr_list.next
            else:
                [curr_list.next, other_list] = [other_list, curr_list.next]
        
        if other_list:
            curr_list.next = other_list
        
        return head
        