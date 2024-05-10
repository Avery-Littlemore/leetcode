# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single 
# digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy = ListNode()
        curr = dummy
        
        adder = 0

        while l1 != None and l2 != None:
            curr.next = ListNode()
            curr = curr.next
            adder += l1.val + l2.val

            if adder < 10:
                curr.val = adder
                adder = 0
            else:
                curr.val = adder - 10
                adder = 1
            
            l1 = l1.next
            l2 = l2.next

        if l1 != None:
            while l1 != None:
                curr.next = ListNode()
                curr = curr.next
                adder += l1.val

                if adder < 10:
                    curr.val = adder
                    adder = 0
                else:
                    curr.val = adder - 10
                    adder = 1
                
                l1 = l1.next

        elif l2 != None:
            while l2 != None:
                curr.next = ListNode()
                curr = curr.next
                adder += l2.val

                if adder < 10:
                    curr.val = adder
                    adder = 0
                else:
                    curr.val = adder - 10
                    adder = 1
                
                l2 = l2.next

        if adder > 0:
            curr.next = ListNode()
            curr = curr.next
            curr.val = adder

        return dummy.next

        