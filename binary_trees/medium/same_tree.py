# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false

# Constraints:
# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        # def helper(p_node, q_node):
        #     if p_node == None or q_node == None:
        #         return p_node == q_node
            
        #     return p_node.val == q_node.val and helper(p_node.left, q_node.left) and helper(p_node.right, q_node.right)
        
        # return helper(p, q)

        if p == None or q == None:
            return p == q

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)