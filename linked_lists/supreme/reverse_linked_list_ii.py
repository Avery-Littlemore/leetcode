# Given the head of a singly linked list and two integers left and right where left <= right, 
# reverse the nodes of the list from position left to position right, and return the reversed list.

# example 1:
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]

# Example 2:
# Input: head = [5], left = 1, right = 1
# Output: [5]

# Follow up: Could you do it in one pass?

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        
        dummy = ListNode(None, head)
        prev = dummy
        curr = head
        n = head.next

        node_num = 1

        while node_num != left:
            prev = curr
            curr = curr.next
            node_num += 1

        conn = prev
        tail = curr

        while node_num <= right:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
            node_num += 1
            
        conn.next = prev
        tail.next = curr

        return dummy.next
