# Given a binary tree, determine if it is height-balanced.
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:
# Input: root = []
# Output: true

# Constraints:
# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        if root == None:
            return True
        def helper(node):
            if node == None:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            
            return 1 + max(left, right)
            
        return helper(root) != -1

# Alternate solution
class Solution(object):
    def isBalanced(self, root):
        if root is None:
            return True
        def depth(node):
            if node is None:
                return 0

            return max(depth(node.left), depth(node.right)) + 1

        left_depth = depth(root.left)
        right_depth = depth(root.right)

        if abs(left_depth - right_depth) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True