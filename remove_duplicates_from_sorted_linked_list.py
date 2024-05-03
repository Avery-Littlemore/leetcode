# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
# Return the linked list sorted as well.

# Input: head = [1,1,2]
# Output: [1,2]

# Input: head = [1,1,2,3,3]
# Output: [1,2,3]


# Constraints:
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

"""
P:
- take the head of a linked list as input
- delete all duplicates
- return the modified linked list

- edge cases:
    - what if an empty list is passed
    - what if a single-item list is passed

E:
Input: head = [1,1,2]
Output: [1,2]

Input: head = [1,1,2,3,3]
Output: [1,2,3]

D:
- use ListNode for nodes

A:
- set prev_node as head
- set current_node as next node
- while current_node.next exists
    - if current node value == prev node value
        - set current node to next node
    - else
        - set prev_node.next to current node
        - set prev node to current node

- if prev_node.val == current_node.val
    - set prev_node.next to None
- else
    - set prev_node.next to current_node
- return head
    
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            prev_node = head
            current_node = prev_node.next
            while current_node.next:
                if current_node.val == prev_node.val:
                    current_node = current_node.next
                else:
                    prev_node.next = current_node
                    prev_node = current_node
            
            if prev_node.val == current_node.val:
                prev_node.next = None
            else:
                prev_node.next = current_node
        
        return head

