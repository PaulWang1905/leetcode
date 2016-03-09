'''
recursion method
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            depth_L = self.maxDepth(root.left)
            depth_R = self.maxDepth(root.right)
        
            return max(depth_L, depth_R)+1
