'''
first left node then right
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        nstack = []
        while root:
            if root.left:
                if root.right:
                    nstack.append(root.right)
                root.right, root.left = root.left, None
            if not root.right and nstack:
                root.right = nstack.pop()
            root = root.right
