# Given the root of a binary tree, invert the tree, and return its root.

# Example 1:
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Example 2:
# Input: root = [2,1,3]
# Output: [2,3,1]

# Example 3:
# Input: root = []
# Output: []

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    # def invertTree(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: TreeNode
    #     """
    #     def invert_helper(node):
    #         if node == None:
    #             return
    #         [node.left, node.right] = [node.right, node.left]

    #         invert_helper(node.left)
    #         invert_helper(node.right)
        
    #     invert_helper(root)

    #     return root
    
    # clever solution
    def invertTree(self, root):
        if root is None:
            return root
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
    
    # left child will be inverted right child (tree)
    # right child will be inverted left child (tree)