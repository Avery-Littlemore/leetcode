# Given the root of a binary tree, flatten the tree into a "linked list":
    # The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
    # The "linked list" should be in the same order as a pre-order traversal of the binary tree.

# Example 1:
# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]

# Example 2:
# Input: root = []
# Output: []

# Example 3:
# Input: root = [0]
# Output: [0]

# Constraints:
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100

# Follow up: Can you flatten the tree in-place (with O(1) extra space)?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def flatten(self, root):
        # if not root:
        #     return []
        
        # result = []
        # stack = [root]

        # while stack:
        #     current = stack.pop()
        #     result.append(current)
        #     if current.right:
        #         stack.append(current.right)
            
        #     if current.left:
        #         stack.append(current.left)

        # for i in range(len(result)):
        #     result[i].left = None
        #     if i == len(result) - 1:
        #         result[i].right = None
        #     else:
        #         result[i].right = result[i + 1]

        # return result

    # in O(1) space complexity, with recursion
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # preorder => NLR
        if root is None:
            return
            
        left = root.left
        right = root.right

        root.left = None
        root.right = left

        while root.right != None:
            root = root.right

        root.right = right

        self.flatten(left)
        self.flatten(right)
