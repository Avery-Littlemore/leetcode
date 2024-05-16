# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. 
# Answers within 10-5 of the actual answer will be accepted.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].

# Example 2:
# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000] 

# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result = []
        def helper(root, level):
            if root is None:
                return
            if len(result) < level:
                result.append([1, [root.val]])
            else:
                result[level - 1][0] += 1
                result[level - 1][1].append(root.val * 1.0)

            helper(root.left, level + 1)
            helper(root.right, level + 1)
        
        helper(root, 1)

        print(result)
        for i in range(len(result)):
            result[i] = sum(result[i][1]) / result[i][0]
            
        return result


# As a queue:
class Solution:
    def averageOfLevels(self, root):
        if root is None:
            return

        queue = [root]
        result = []
        while queue:
            # the length of the row is what is in the queue
            row_length = len(queue)
            row_sum = 0
            # for the entire row's length
            for i in range(row_length):
                node = queue.pop(0)
                row_sum += node.val

                # if the node has a left child add it to the queue
                if node.left is not None:
                    queue.append(node.left)

                # if the node has a right child add it to the queue
                if node.right is not None:
                    queue.append(node.right)
            
            result.append(row_sum/row_length)

        return result

# tree
#      [3]      => 3  / 1 == 3
#   [9    20]   => 29 / 2 == 14.5
# [15 7 15   7] => 44 / 4 == 11.25

# queue      == [3]
# row_length == 1
# row_sum    == 0

# for the whole row's length
# pop one from the front of the queue and save it to a variable `node`
# queue      == []
# add it to the row sum
# row_sum    == 3
# if node has left children, add them to the queue
# [9]
# if the node has right children, add them to the queue
# [9, 20]
# do your math and add the result to an array to return later
# reset `row_sum`

# queue      == [9, 20]
# row_length == 2
# row_sum    == 0

# pop one from the front of the queue and save it to a variable `node`
# queue      == [20]
# add it to row sum
# row_sum    == 9
# add it's left and right children to the queue
# queue      == [20, 15, 7]
# pop one from the front of the queue and save it to a variable `node` (a second time since row's length is 2)
# queue      == [15, 7]
# add it to row sum
# add it's left and right children to the queue
# queue      == [15, 7, 15, 7]
# do math

# etc.....
# profit ????