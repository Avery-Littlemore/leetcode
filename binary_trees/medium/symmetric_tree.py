# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false

# Constraints:
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isMirror(self, left, right):
        if left == None or right == None:
            return left == right
        
        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
        
    def isSymmetric(self, root):
        return self.isMirror(root.left, root.right)
    

    # def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    #     def symmetric_helper(left, right):
    #         # if both are None, they are symmetric by definition
    #         if left is None and right is None:
    #             return True

    #         # if one is None and the other isn't, it's not symmetric
    #         if left is None or right is None:
    #             return False

    #         # if the right node's value is not equal to the left node's value, it's not symmetric
    #         if right.val != left.val:
    #             return False

    #         return symmetric_helper(left.left, right.right) and symmetric_helper(left.right, right.left)
        
    #     if root is None:
    #         return True

    #     return symmetric_helper(root.left, root.right)

    