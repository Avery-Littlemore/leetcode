# Given the root of a binary tree, return the leftmost value in the last row of the tree.

# Example 1:
# Input: root = [2,1,3]
# Output: 1

# Example 2:
# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7
 
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findBottomLeftValue(self, root):

        # result = [val, level]
        result = [root.val, 0]

        def dfs(root, level):
            if root == None:
                return 
            
            if result[1] < level:
                result[0] = root.val
                result[1] = level

            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)

        return result[0]
    
    # def findBottomLeftValue(self, root):
    #     queue = deque()
    #     queue.append([root])

    #     while queue:
    #         new_level = []
    #         current_level = queue.popleft()
    #         is_last_level = True
            
    #         for node in current_level:
    #             if node.left or node.right:
    #                 is_last_level = False

    #                 if node.left:
    #                     new_level.append(node.left)
    #                 if node.right:
    #                     new_level.append(node.right)

    #         if is_last_level:
    #             return current_level[0].val

    #         queue.append(new_level)