# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root) != -1
    
    def dfs(self, root):
        if root:
            ld = self.dfs(root.left)
            if ld == -1:
                return -1
            rd = self.dfs(root.right)
            if rd == -1:
                return -1
            return max(ld, rd) + 1 if -1 <= ld-rd <= 1 else -1
        else:
            return 0
