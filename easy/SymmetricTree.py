# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            left = self.leftOrder(root.left)
            right = self.rightOrder(root.right)
            return left == right
        return True
    
    def leftOrder(self, root):
        rst = []
        stack = []
        stack.append(root)
        while stack:
            top = stack.pop()
            if top:
                rst.append(top.val)
                stack.append(top.right)
                stack.append(top.left)
            else:
                rst.append(None)
        return rst
    def rightOrder(self, root):
        rst = []
        stack = []
        stack.append(root)
        while stack:
            top = stack.pop()
            if top:
                rst.append(top.val)
                stack.append(top.left)
                stack.append(top.right)
            else:
                rst.append(None)
        return rst
