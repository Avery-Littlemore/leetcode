# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

# Example 2:
# Input: root = [1,null,3]
# Output: [1,3]

# Example 3:
# Input: root = []
# Output: [] 

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root):
        """
        BFS
        - create a queue
        - add the root to the queue
        - initialize right_side list of values

        - while queue
            - add front-most value in the queue to the right_side list
            - set current_length to current length of queue
            
            - for node in queue:
                - pop the front-most node

                - if there is a right child
                    - queue the right child 
                - if there is a left child
                    - queue the left child

        - return right_side list
        """

        if not root:
            return root

        queue = collections.deque([root])
        right_side_vals = []

        while queue:
            right_side_vals.append(queue[0].val)
            current_length = len(queue)

            for _ in range(current_length):
                node = queue.popleft()

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

        return right_side_vals

