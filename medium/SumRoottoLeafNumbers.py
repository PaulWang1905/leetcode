# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(0, root)
    
    def helper(self, sum, root):
        if not root:
            return 0
        sum = sum * 10 + root.val
        if not root.left and not root.right:
            return sum
        else:
            return self.helper(sum, root.left) + self.helper(sum, root.right)
