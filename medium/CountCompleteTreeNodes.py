# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            rst = 1
            for i in range(self.leftDepth(root)-1, 0, -1):
                rst <<= 1
                if i == self.leftDepth(root.right):
                    rst |= 1
                    root = root.right
                else:
                    root = root.left
            return rst
        return 0
        
    def leftDepth(self, root):
        level = 0
        while root:
            level += 1
            root = root.left
        return level
