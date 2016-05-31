# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rst = []
        stack = []
        stack.append(root)
        while stack:
            top = stack.pop()
            if top:
                rst.append(top.val)
                stack.append(top.right)
                stack.append(top.left)
        return rst
